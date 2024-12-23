#!/usr/bin/env python

import time
import os
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import json
import sys
import re

# SET VARIABLES FROM CONTAINER ENVIRONMENT
SLEEP_TIME_SIDECAR = 5 if os.getenv("SLEEP_TIME_SIDECAR") is None else int(
    re.sub("[A-z]", "", os.getenv("SLEEP_TIME_SIDECAR")))
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
URL = os.getenv("URL")
# REQUEST CONNECTION PARAMETERS
FLOW_REQ_RETRY_TOTAL = 20 if os.getenv("REQ_RETRY_TOTAL") is None else int(os.getenv("REQ_RETRY_TOTAL"))
FLOW_REQ_RETRY_CONNECT = 30 if os.getenv("REQ_RETRY_CONNECT") is None else int(os.getenv("REQ_RETRY_CONNECT"))
FLOW_REQ_RETRY_READ = 15 if os.getenv("REQ_RETRY_READ") is None else int(os.getenv("REQ_RETRY_READ"))
FLOW_REQ_RETRY_BACKOFF_FACTOR = 1.1 if os.getenv("REQ_RETRY_BACKOFF_FACTOR") is None else float(
    os.getenv("REQ_RETRY_BACKOFF_FACTOR"))
FLOW_REQ_TIMEOUT = 60 if os.getenv("REQ_TIMEOUT") is None else float(os.getenv("REQ_TIMEOUT"))
FLOW_REQ_TLS_VERIFY = False if os.getenv("REQ_SKIP_TLS_VERIFY") == "true" else None

EXTRA_NODE_MODULES = None if os.path.isfile('/data/extra-node-modules.json') is False else json.load(
    (open('/data/extra-node-modules.json', "r")))
script_errors = {}


def main():
    print("----START PYTHON SIDECAR SCRIPT----")
    print("node-red node module install and flow refresh api call via k8s-sidecar")
    print(f"sidecar sleeping for {SLEEP_TIME_SIDECAR} seconds...")
    time.sleep(SLEEP_TIME_SIDECAR)

    # REQUESTS INIT SESSION
    r = requests.Session()
    retries = Retry(
        total=FLOW_REQ_RETRY_TOTAL,
        connect=FLOW_REQ_RETRY_CONNECT,
        read=FLOW_REQ_RETRY_READ,
        backoff_factor=FLOW_REQ_RETRY_BACKOFF_FACTOR,
    )
    r.mount("http://", HTTPAdapter(max_retries=retries))
    r.mount("https://", HTTPAdapter(max_retries=retries))

    # Make the request
    authenticationScheme = r.get(
        "%s" % URL + "/auth/login",
    )

    try:
        data = authenticationScheme.json()
    except json.JSONDecodeError:
        print("Received non-JSON response.")
        sys.exit(1)

    # Check if the data is an empty object
    if data == {}:
        print("Empty authentication scheme response.")
        token = None
    else:
        # GET NODE RED BEARER TOKEN
        print("----TOKEN----")
        payload_token = {
            "client_id": "node-red-admin",
            "grant_type": "password",
            "scope": "*",
            "username": USERNAME,
            "password": PASSWORD,
        }
        r_token = r.post(
            "%s" % URL + "/auth/token",
            data=payload_token,
            timeout=FLOW_REQ_TIMEOUT,
            verify=FLOW_REQ_TLS_VERIFY,
        )
        if r_token.status_code == requests.codes.ok:
            print(f"node-red bearer token successfully created - {r_token.status_code}")
            token = json.loads(r_token.text)["access_token"]
        else:
            print(f"could not create bearer token.... {r_token.status_code}")
            sys.exit(r_token.status_code)

    # NODE MODULE INSTALL VIA HELM SIDECAR EXTRA NODE MODULES CONFIG MAP
    print("----INSTALL EXTRA NODE MODULES----")
    if EXTRA_NODE_MODULES is not None:
        print(f"found extra node modules in configmap - {EXTRA_NODE_MODULES}")
        # GET ISNTALLED NODE MODULES
        headers_node_module = {
            "Accept": "application/json",
        }
        if token:
            # If token has a value, add Authorization to headers
            headers_node_module["Authorization"] = "Bearer" + " " + token
        r_node_modules = r.get(
            "%s" % URL + "/nodes",
            headers=headers_node_module,
            timeout=FLOW_REQ_TIMEOUT,
            verify=FLOW_REQ_TLS_VERIFY,
        )
        node_modules = json.loads(r_node_modules.text)
        # PARSE ALL INSTALLED MODULES FROM EVERY ARRAY AN SET AS UNIQUE LIST FROM AKTIVE NODE RED DEPLOYEMNT
        modules_installed = list(set([item.get("module") for item in node_modules]))
        print(f"currently installed node modules - {modules_installed}")

        for module in EXTRA_NODE_MODULES:
            if module not in modules_installed:
                try:
                    module_name, version = module.rsplit('/', 1)[-1].split('@', 1) if '@' in module else (module, None)
                except:
                    module_name, version = module, None
                payload_node_module = ''
                if version is not None:
                    payload_node_module = '{"module": "' + module_name + '", "version": "' + version + '"}'
                else:
                    payload_node_module = '{"module": "' + module_name + '"}'
                headers_node_module = {
                    "Content-type": "application/json",
                }
                if token:
                    # If token has a value, add Authorization to headers
                    headers_node_module["Authorization"] = "Bearer" + " " + token
                # INSTALL NODE MODULES FROM ITERATION
                r_node_modules = r.post(
                    "%s" % URL + "/nodes",
                    headers=headers_node_module,
                    data=payload_node_module,
                    timeout=FLOW_REQ_TIMEOUT,
                    verify=FLOW_REQ_TLS_VERIFY,
                )
                if r_node_modules.status_code == requests.codes.ok:
                    print(f"node module {module} successfully installed -  {r_node_modules.status_code}")
                else:
                    print(f"error-status-code = {r_node_modules.status_code} while installing {module}")
                    script_errors.update({module: r_node_modules.status_code})
                    # sys.exit at the end! Non hard exit.
            else:
                print(f"node module {module} already installed...")
    else:
        print("no extra node-modules found from configmap ...")
        print("skipping extra node modules installation...")

    # FLOW REFRESH/RELOAD FLOWS FROM SECRET/CONFIGMAP
    print("----RELOAD FLOWS----")
    payload_flow_refresh = '{"flows": [{"type": "tab"}]}'
    headers_flow_refresh = {
        "content-type": "application/json; charset=utf-8",
        "Node-RED-Deployment-Type": "reload",
        "Node-RED-API-Version": "v2",
    }
    if token:
        # If token has a value, add Authorization to headers
        headers_flow_refresh["Authorization"] = "Bearer" + " " + token

    r_flow_refresh = r.post(
        "%s" % URL + "/flows",
        headers=headers_flow_refresh,
        data=payload_flow_refresh,
        timeout=FLOW_REQ_TIMEOUT,
        verify=FLOW_REQ_TLS_VERIFY,
    )

    if r_flow_refresh.status_code == requests.codes.ok:
        print(f"node-red flows successfully reloaded - {r_flow_refresh.status_code}")
    else:
        print(f"could not refresh flows - {r_flow_refresh.status_code}")
        script_errors.update({"flow_refresh": r_flow_refresh.status_code})
        # sys.exit(r_flow_refresh.status_code)

    # NODE MODULE INSTALL VIA HELM SIDECAR EXTRA ENVIROMENT
    print("----SCRIPT EXIT----")
    if script_errors:
        print(json.dumps(script_errors, indent=4))
        sys.exit("script errors found...")
    else:
        print("no script errors found...")
        sys.exit(0)


if __name__ == "__main__":
    main()
