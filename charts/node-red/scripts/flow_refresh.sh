#!/bin/sh
echo "node-red flow refresh api"
sleep $SLEEP_TIME_SIDECAR
token=$(curl -X POST -sSk --connect-timeout 30 --retry 50 --retry-delay 10 --data "client_id=node-red-admin&grant_type=password&scope=*&username=$USERNAME&password=$PASSWORD" $URL/auth/token | grep "^{" |  jq -r .access_token)
curl -k -X POST --connect-timeout 30 --retry 50 --retry-delay 10 -H "Authorization: Bearer $token" -H "content-type: application/json; charset=utf-8" -H "Node-RED-Deployment-Type: reload" -H "Node-RED-API-Version: v2"  --data '{"flows": [{"type": "tab"}]}' $URL/flows
