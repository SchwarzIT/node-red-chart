#!/usr/bin/env python

import time
import os
import requests
import json
import sys
import re

# SET VARIABLES FROM CONTAINER ENVIRONMENT
SLEEP_TIME_SIDECAR = 5 if os.getenv("SLEEP_TIME_SIDECAR") is None else int(re.sub('[A-z]', "",os.getenv("SLEEP_TIME_SIDECAR")))
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
URL = os.getenv("URL")

print('node-red flow refresh api call via k8s-sidecar')
print('sidecar sleeping for', SLEEP_TIME_SIDECAR, 'seconds...')
time.sleep(SLEEP_TIME_SIDECAR)

# GET NODE RED BEARER TOKEN
PAYLOAD_TOKEN = {"client_id": "node-red-admin", "grant_type": "password", "scope": "*", "username": USERNAME, "password": PASSWORD}
r_token = requests.post(URL + '/auth/token', data=PAYLOAD_TOKEN, timeout=30)
if r_token.status_code == requests.codes.ok:
    print('node-red bearer token successfully created -', r_token.status_code)  
    token = (json.loads(r_token.text)["access_token"])
else:
    print('could not create bearer token....', r_token.status_code) 
    sys.exit('Error-Code -', r_token.status_code)

# FLOW REFRESH/RELOAD FLOWS FROM SECRET/CONFIGMAP
PAYLOAD_FLOW_REFRESH = "{\"flows\": [{\"type\": \"tab\"}]}"
HEADERS_FLOW_REFRESH={
  'Authorization': 'Bearer' + ' ' + token,
  'content-type': 'application/json; charset=utf-8',
  'Node-RED-Deployment-Type': 'reload',
  'Node-RED-API-Version': 'v2'
}

r_flow_refresh = requests.post(URL + '/flows', headers=HEADERS_FLOW_REFRESH, data=PAYLOAD_FLOW_REFRESH, timeout=30) 

if r_flow_refresh.status_code == requests.codes.ok:
    print('node-red flows successfully reloaded -', r_flow_refresh.status_code)
    sys.exit(0)   
else:
    sys.exit('Error-Code', r_flow_refresh.status_code)