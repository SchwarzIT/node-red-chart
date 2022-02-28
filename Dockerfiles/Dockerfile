ARG VERSION_DOCKER=2.2.2
FROM nodered/node-red:$VERSION_DOCKER
RUN npm install passport-openidconnect@0.1.1
RUN npm install passport-oauth2@1.6.1
RUN npm install --no-update-notifier --no-fund --save-prefix=~ --production --engine-strict node-red-contrib-opcua@0.2.258
RUN npm install --no-update-notifier --no-fund --save-prefix=~ --production --engine-strict node-red-contrib-prometheus-exporter@1.0.5
RUN npm install --no-update-notifier --no-fund --save-prefix=~ --production --engine-strict node-red-contrib-minio-all@0.0.6