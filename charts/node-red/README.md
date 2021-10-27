# node-red ⚙

![Version: 0.3.0](https://img.shields.io/badge/Version-0.3.0-informational?style=flat-square)
![AppVersion: 2.1.3](https://img.shields.io/badge/AppVersion-2.1.3-informational?style=flat-square)
![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)
[![Linting and Testing](https://github.com/dirien/node-red-chart/actions/workflows/lint-and-test.yml/badge.svg)](https://github.com/dirien/node-red-chart/actions/workflows/lint-and-test.yml)
[![Artifact Hub](https://img.shields.io/endpoint?url=https://artifacthub.io/badge/repository/node-red)](https://artifacthub.io/packages/search?repo=node-red)
[![SIT](https://img.shields.io/badge/SIT-awesome-blueviolet.svg)](https://jobs.schwarz)


<img src="https://nodered.org/about/resources/media/node-red-icon-2.png" width="80" height="80">

A Helm chart for Node-Red, a low-code programming for event-driven applications

**Homepage:** <https://nodered.org/>

## Usage
Adding node-red repository
Before installing any chart provided by this repository, add the node-red Charts Repository:

```bash
helm repo add node-red https://schwarzit.github.io/node-red-chart/
helm repo update
```

## Installing the Chart
To install the chart with the release name node-red run:

```bash
helm install node-red node-red/node-red
```

After a few seconds, node-red should be running.

To install the chart in a specific namespace use following commands:

```bash
kubectl create ns node-red 
helm install node-red node-red/node-red --namespace node-red
```

> **Tip**: List all releases using `helm list`, a release is a name used to track a specific deployment

## Uninstalling the Chart

To uninstall the `node-red` deployment:

```bash
helm uninstall node-red
```

The command removes all the Kubernetes components associated with the chart and deletes the release.

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` | The affinity constraint |
| env | list | `[]` | node-red env, see more environment variables in the [node-red documentation](https://nodered.org/docs/getting-started/docker) |
| fullnameOverride | string | `""` | String to fully override "node-red.fullname" |
| image.pullPolicy | string | `"IfNotPresent"` | The image pull policy |
| image.registry | string | `"docker.io"` | The image registry to pull from |
| image.repository | string | `"nodered/node-red"` | The image repository to pull from |
| image.tag | string | `""` | The image tag to pull, default: `Chart.appVersion` |
| imagePullSecrets | string | `""` | The image pull secrets |
| ingress.annotations | object | `{}` | Additional ingress annotations |
| ingress.className | string | `""` | Defines which ingress controller will implement the resource |
| ingress.enabled | bool | `false` | Enable an ingress resource for the server |
| ingress.hosts[0].host | string | `"chart-example.local"` | Ingress accepted hostnames |
| ingress.hosts[0].paths[0].path | string | `"/"` | The base path |
| ingress.hosts[0].paths[0].pathType | string | `"ImplementationSpecific"` | Ingress type of path |
| ingress.tls | list | `[]` | Ingress TLS configuration |
| nameOverride | string | `"node-red"` | Provide a name in place of node-red |
| npmrc.enabled | bool | `false` | Enable custom npmrc config |
| npmrc.registry | string | `"https://registry.npmjs.org"` | Configuration to use any compatible registry |
| nodeSelector | object | `{}` | Node selector |
| persistence.accessMode | string | `"ReadWriteOnce"` | Persistence access modes |
| persistence.enabled | bool | `false` | Use persistent volume to store data |
| persistence.storageClass | string | `"-"` | Type of persistent volume claim |
| persistence.existingClaim | string | `""` | Use an existing PVC to persist data |
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
| serviceAccount.name | string | `"default"` | Service account name to use, when empty will be set to created account if serviceAccount.create is set else to default |
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

### Contributing 🤝

#### Contributing via GitHub

Feel free to join. Checkout the [contributing guide](CONTRIBUTING.md)

#### License

Apache License, Version 2.0

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| [@dirien](https://github.com/dirien) | engin.diri@mail.schwarz | https://jobs.schwarz |