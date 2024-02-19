# node-red ⚙

![Version: 0.28.1](https://img.shields.io/badge/Version-0.28.1-informational?style=for-the-badge) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=for-the-badge) ![AppVersion: 3.0.2](https://img.shields.io/badge/AppVersion-3.0.2-informational?style=for-the-badge)

[![Artifact Hub](https://img.shields.io/endpoint?url=https://artifacthub.io/badge/repository/node-red&style=for-the-badge)](https://artifacthub.io/packages/search?repo=node-red)
[![SIT](https://img.shields.io/badge/SIT-awesome-blueviolet.svg?style=for-the-badge)](https://jobs.schwarz)

<img src="https://nodered.org/about/resources/media/node-red-icon-2.png" width="80" height="80">

## Description 📜

A Helm chart for Node-Red, a low-code programming for event-driven applications

## Usage (via OCI Registry)

To install the chart using the OCI artifact, run:

```bash
helm install node-red oci://ghcr.io/schwarzit/charts/node-red --version 0.28.1
```

## Usage
Adding node-red repository
Before installing any chart provided by this repository, add the node-red Charts Repository:

```bash
helm repo add node-red https://schwarzit.github.io/node-red-chart/
helm repo update
```

### Installing the Chart 📦
To install the chart with the release name node-red run:

```bash
helm install node-red node-red/node-red --version 0.28.1
```

After a few seconds, node-red should be running.

To install the chart in a specific namespace use following commands:

```bash
kubectl create ns node-red
helm install node-red node-red/node-red --namespace node-red
```

> **Tip**: List all releases using `helm list`, a release is a name used to track a specific deployment

### Uninstalling the Chart 🗑️

To uninstall the `node-red` deployment:

```bash
helm uninstall node-red
```

The command removes all the Kubernetes components associated with the chart and deletes the release.

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` | The affinity constraint |
| clusterRoleRules.enabled | bool | `false` | Enable custom rules for the application controller's ClusterRole resource default: false |
| clusterRoleRules.rules | list | `[]` | List of custom rules for the application controller's ClusterRole resource default: [] |
| createClusterRole | bool | `false` | Create a ClusterRole resource for the node-red pod. default: false |
| deploymentAnnotations | object | `{}` | Deployment annotations |
| deploymentStrategy | string | `""` | Specifies the strategy used to replace old Pods by new ones, default: `RollingUpdate` |
| env | list | `[]` | node-red env, see more environment variables in the [node-red documentation](https://nodered.org/docs/getting-started/docker) |
| envFrom | list | `[]` |  |
| extraSidecars | list | `[]` | You can configure extra sidecars containers to run alongside the node-red pod. default: [] |
| extraVolumeMounts | string | `nil` | Extra Volume Mounts for the node-red pod |
| extraVolumes | string | `nil` | Extra Volumes for the pod |
| fullnameOverride | string | `""` | String to fully override "node-red.fullname" |
| image.pullPolicy | string | `"IfNotPresent"` | The image pull policy |
| image.registry | string | `"docker.io"` | The image registry to pull from |
| image.repository | string | `"nodered/node-red"` | The image repository to pull from |
| image.tag | string | `""` | The image tag to pull, default: `Chart.appVersion` |
| imagePullSecrets | string | `""` | The image pull secrets |
| ingress.annotations | object | `{}` | Additional ingress annotations |
| ingress.className | string | `""` | Defines which ingress controller will implement the resource |
| ingress.enabled | bool | `false` | Enable an ingress resource for the server |
| ingress.hosts[0].host | string | `"chart-example.local"` |  |
| ingress.hosts[0].paths[0] | object | `{"path":"/","pathType":"ImplementationSpecific"}` | The base path |
| ingress.hosts[0].paths[0].pathType | string | `"ImplementationSpecific"` | Ingress type of path |
| ingress.tls | list | `[]` | Ingress TLS configuration |
| initContainers | list | `[]` | containers which are run before the app containers are started |
| livenessProbe | object | `{"httpGet":{"path":"/","port":"http"}}` | Liveness probe for the Deployment |
| metrics.enabled | bool | `false` | Deploy metrics service |
| metrics.path | string | `"/metrics"` |  |
| metrics.serviceMonitor.additionalLabels | object | `{}` | Prometheus ServiceMonitor labels |
| metrics.serviceMonitor.basicAuth | object | `{}` | Prometheus basicAuth configuration for ServiceMonitor endpoint |
| metrics.serviceMonitor.enabled | bool | `false` | Enable a prometheus ServiceMonitor |
| metrics.serviceMonitor.interval | string | `"30s"` | Prometheus ServiceMonitor interval |
| metrics.serviceMonitor.metricRelabelings | list | `[]` | Prometheus [MetricRelabelConfigs] to apply to samples before ingestion |
| metrics.serviceMonitor.namespace | string | `""` | Prometheus ServiceMonitor namespace |
| metrics.serviceMonitor.relabelings | list | `[]` | Prometheus [RelabelConfigs] to apply to samples before scraping |
| metrics.serviceMonitor.selector | object | `{}` | Prometheus ServiceMonitor selector |
| nameOverride | string | `""` | Provide a name in place of node-red |
| nodeSelector | object | `{}` | Node selector |
| npmrc.content | string | `"# Custom npmrc config\n"` | Configuration to add custom npmrc config |
| npmrc.enabled | bool | `false` | Enable custom npmrc config |
| npmrc.registry | string | `"https://registry.npmjs.org"` | Configuration to use any compatible registry |
| persistence.accessMode | string | `"ReadWriteOnce"` | Persistence access mode |
| persistence.enabled | bool | `false` | Use persistent volume to store data |
| persistence.keepPVC | bool | `false` | ## Keep a created Persistent volume claim when uninstalling the helm chart (default: false) |
| persistence.size | string | `"5Gi"` | Size of persistent volume claim |
| podAnnotations | object | `{}` | Pod annotations |
| podLabels | object | `{}` | Labels to add to the node-red pod. default: {} |
| podSecurityContext | object | `{"fsGroup":1000,"runAsUser":1000}` | Pod Security Context see [values.yaml](values.yaml) |
| podSecurityContext.fsGroup | int | `1000` | node-red group is 1000 |
| podSecurityContext.runAsUser | int | `1000` | node-red user is 1000 |
| readinessProbe | object | `{"httpGet":{"path":"/","port":"http"}}` | Readiness probe for the Deployment |
| resources | object | `{"limits":{"cpu":"500m","memory":"5123Mi"},"requests":{"cpu":"100m","memory":"128Mi"}}` | CPU/Memory resource requests/limits |
| securityContext | object | `{"allowPrivilegeEscalation":false,"capabilities":{"drop":["ALL"]},"privileged":false,"readOnlyRootFilesystem":true,"runAsGroup":10003,"runAsNonRoot":true,"runAsUser":10003,"seccompProfile":{"type":"RuntimeDefault"}}` | Security Context see [values.yaml](values.yaml) |
| service.annotations | object | `{}` | Annotations for the service |
| service.port | int | `1880` | Kubernetes port where service is exposed |
| service.type | string | `"ClusterIP"` | Kubernetes service type |
| serviceAccount.annotations | object | `{}` | Additional ServiceAccount annotations |
| serviceAccount.create | bool | `true` | Create service account |
| serviceAccount.name | string | `""` | Service account name to use, when empty will be set to created account if |
| settings | object | `{}` | You can configure node-red using a settings file. default: {} |
| sidecar.enabled | bool | `false` | Enable the sidecar |
| sidecar.env.label | string | `"node-red-settings"` | Label that should be used for filtering |
| sidecar.env.label_value | string | `"1"` | The value for the label you want to filter your resources on. Don't set a value to filter by any value |
| sidecar.env.method | string | `"watch"` | If METHOD is set to LIST, the sidecar will just list config-maps/secrets and exit. With SLEEP it will list all config-maps/secrets, then sleep for SLEEP_TIME seconds. Anything else will continuously watch for changes (see https://kubernetes.io/docs/reference/using-api/api-concepts/#efficient-detection-of-changes). |
| sidecar.env.password | string | `""` | Password as key value pair |
| sidecar.env.passwordFromExistingSecret | object | `{}` | Password from existing secret |
| sidecar.env.script | string | `"flow_refresh.py"` | Absolute path to shell script to execute after a configmap got reloaded. |
| sidecar.env.sleep_time_sidecar | string | `"5s"` | Set the sleep time for refresh script |
| sidecar.env.username | string | `""` |  |
| sidecar.extraEnv | list | `[]` | Extra Environments for the sidecar |
| sidecar.extraNodeModules | list | `[]` | Extra Node-Modules that will be installed from the sidecar script (specifying a version like node-red-contrib-example@1.2.3 is supported) |
| sidecar.image.pullPolicy | string | `"IfNotPresent"` | The image pull policy, default: `IfNotPresent` |
| sidecar.image.registry | string | `"quay.io"` | The image registry to pull the sidecar from |
| sidecar.image.repository | string | `"kiwigrid/k8s-sidecar"` | The image repository to pull from |
| sidecar.image.tag | string | `"1.25.3"` | The image tag to pull, default: `1.25.3` |
| sidecar.resources | object | `{}` | Resources for the sidecar |
| sidecar.securityContext | object | `{}` | Security context for the sidecar |
| sidecar.volumeMounts | list | `[]` | The extra volume mounts for the sidecar |
| terminationGracePeriodSeconds | int | `30` | The terminationGracePeriodSeconds for the pod here we explicitly set the default value defined in kubernetes https://github.com/kubernetes/api/blob/d4b94f478bb2e6467873657dd7b4e1b0ac8351be/core/v1/types.go#L3114-L3118 |
| tolerations | list | `[]` | Toleration labels for pod assignment |

Specify each parameter using the `--set key=value[,key=value]` argument to `helm install`. For example,

```bash
helm install node-red node-red/node-red --set image.tag=latest
```

Alternatively, a YAML file that specifies the values for the parameters can be provided while installing the chart. For example,

```bash
helm install node-red node-red/node-red -f values.yaml
```

> **Tip**: You can use the default [values.yaml](values.yaml)

## Monitoring 🌡️
To enable the node-red prometheus monitoring capability, you need to install the node `node-red-contrib-prometheus-exporter`.
For more details see [official documentation](https://flows.nodered.org/node/node-red-contrib-prometheus-exporter)

In the helm value you can enable the `ServiceMonitor` via

```yaml
metrics:
  enabled: true
  serviceMonitor:
    enabled: true
```

## Sidecar 🏎️

This Chart supports the handling for loading flows from configmaps/secrets via the [k8s-sidecar](https://github.com/kiwigrid/k8s-sidecar)

You just need to create a configmap/secret with your `node-red` flow.json and annotate it with the a label and value defined in the chart `sidecar`.
Default values are: `node-red-settings:1`.

The `k8s-sidecar` will then call the `node-red` api to reload the flows. This will be done via a script. To run this script successfully you need to provide the `username` and `password`
of your admin user. The admin user needs to have the right to use the `node-red` API.

The `k8s-sidecar` can also call the `node-red` api to install additional node modules (npm packages) before refreshing or importing the flow.json. Specifying a version for a module is supported (s. example below).
You need to list your flows requiert 'NODE_MODULES' in the `sidecar.extraNodeModules`: e.g.

```yaml
sidecar:
 extraNodeModules:
    - node-red-contrib-xkeys_setunitid
    - node-red-contrib-microsoft-teams-tasks
    - node-red-contrib-json@0.2.0
```
To install the node modules successfully, the node red pod needs access to the `npmrc.registry` to download the declaired modules/packages.

## Contributing 🤝

### Contributing via GitHub

Feel free to join. Checkout the [contributing guide](CONTRIBUTING.md)

## License ⚖️

Apache License, Version 2.0

## Source Code

* <https://github.com/SchwarzIT/node-red-chart>

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| dirien | <engin@pulumi.com> | <https://pulumi.com> |
| Kaktor | <felix.kammerer@mail.schwarz> | <https://jobs.schwarz> |
