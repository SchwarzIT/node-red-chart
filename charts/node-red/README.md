# node-red ⚙

![Version: 0.13.0](https://img.shields.io/badge/Version-0.13.0-informational?style=for-the-badge)
![Type: application](https://img.shields.io/badge/Type-application-informational?style=for-the-badge) 
![AppVersion: 2.2.2](https://img.shields.io/badge/AppVersion-2.2.2-informational?style=for-the-badge) 

[![Artifact Hub](https://img.shields.io/endpoint?url=https://artifacthub.io/badge/repository/node-red&style=for-the-badge)](https://artifacthub.io/packages/search?repo=node-red)
[![SIT](https://img.shields.io/badge/SIT-awesome-blueviolet.svg?style=for-the-badge)](https://jobs.schwarz)


<img src="https://nodered.org/about/resources/media/node-red-icon-2.png" width="80" height="80">

## Description

A Helm chart for Node-Red, a low-code programming for event-driven applications

## Usage
Adding node-red repository
Before installing any chart provided by this repository, add the node-red Charts Repository:

```bash
helm repo add node-red https://schwarzit.github.io/node-red-chart/
helm repo update
```

### Installing the Chart
To install the chart with the release name node-red run:

```bash
helm install node-red node-red/node-red --version 0.13.0
```

After a few seconds, node-red should be running.

To install the chart in a specific namespace use following commands:

```bash
kubectl create ns node-red 
helm install node-red node-red/node-red --namespace node-red
```

> **Tip**: List all releases using `helm list`, a release is a name used to track a specific deployment

### Uninstalling the Chart

To uninstall the `node-red` deployment:

```bash
helm uninstall node-red
```

The command removes all the Kubernetes components associated with the chart and deletes the release.

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` | The affinity constraint |
| deploymentStrategy | string | `""` | Specifies the strategy used to replace old Pods by new ones, default: `RollingUpdate` |
| env | list | `[]` | node-red env, see more environment variables in the [node-red documentation](https://nodered.org/docs/getting-started/docker) |
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
| ingress.hosts[0] | object | `{"host":"chart-example.local","paths":[{"path":"/","pathType":"ImplementationSpecific"}]}` | Ingress accepted hostnames |
| ingress.hosts[0].paths[0] | object | `{"path":"/","pathType":"ImplementationSpecific"}` | The base path |
| ingress.hosts[0].paths[0].pathType | string | `"ImplementationSpecific"` | Ingress type of path |
| ingress.tls | list | `[]` | Ingress TLS configuration |
| initContainers | list | `[]` | containers which are run before the app containers are started |
| metrics | object | `{"enabled":false,"path":"/metrics","serviceMonitor":{"additionalLabels":{},"enabled":false,"interval":"30s","metricRelabelings":[],"namespace":"","relabelings":[],"selector":{}}}` | Enable Service-Monitor for node-red |
| metrics.enabled | bool | `false` | Deploy metrics service |
| metrics.serviceMonitor.additionalLabels | object | `{}` | Prometheus ServiceMonitor labels |
| metrics.serviceMonitor.enabled | bool | `false` | Enable a prometheus ServiceMonitor |
| metrics.serviceMonitor.interval | string | `"30s"` | Prometheus ServiceMonitor interval |
| metrics.serviceMonitor.metricRelabelings | list | `[]` | Prometheus [MetricRelabelConfigs] to apply to samples before ingestion |
| metrics.serviceMonitor.namespace | string | `""` | Prometheus ServiceMonitor namespace |
| metrics.serviceMonitor.relabelings | list | `[]` | Prometheus [RelabelConfigs] to apply to samples before scraping |
| metrics.serviceMonitor.selector | object | `{}` | Prometheus ServiceMonitor selector |
| nameOverride | string | `""` | Provide a name in place of node-red |
| nodeSelector | object | `{}` | Node selector |
| npmrc.enabled | bool | `false` | Enable custom npmrc config |
| npmrc.registry | string | `"https://registry.npmjs.org"` | Configuration to use any compatible registry |
| persistence.accessMode | string | `"ReadWriteOnce"` | Persistence access mode |
| persistence.enabled | bool | `false` | Use persistent volume to store data |
| persistence.size | string | `"5Gi"` | Size of persistent volume claim |
| podAnnotations | object | `{}` | Pod annotations |
| podSecurityContext | object | `{}` | Pod Security Context see [values.yaml](values.yaml) |
| replicaCount | int | `1` | Number of nodes |
| resources | object | `{}` | CPU/Memory resource requests/limits |
| securityContext | object | `{}` | Security Context see [values.yaml](values.yaml) |
| service.port | int | `1880` | Kubernetes port where service is exposed |
| service.type | string | `"ClusterIP"` | Kubernetes service type |
| serviceAccount.annotations | object | `{}` | Additional ServiceAccount annotations |
| serviceAccount.create | bool | `true` | Create service account |
| serviceAccount.name | string | `""` | Service account name to use, when empty will be set to created account if |
| settings | object | `{}` | You can configure node-red using a settings file. default: {} |
| sidecars | list | `[]` | You can configure a sidecar containers to run alongside the node-red pod. default: [] |
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

## Monitoring
To enable the node-red prometheus monitoring capability, you need to install the node `node-red-contrib-prometheus-exporter`.
For more details see [official documentation](https://flows.nodered.org/node/node-red-contrib-prometheus-exporter)

In the helm value you can enable the `ServiceMonitor` via

```yaml
metrics:
  enabled: true
  serviceMonitor:
    enabled: true
```

## Contributing 🤝

### Contributing via GitHub

Feel free to join. Checkout the [contributing guide](CONTRIBUTING.md)

## License

Apache License, Version 2.0

## Source Code

* <https://github.com/SchwarzIT/node-red-chart>

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| dirien | engin.diri@mail.schwarz | https://jobs.schwarz |
| Kaktor | felix.kammerer@mail.schwarz | https://jobs.schwarz |