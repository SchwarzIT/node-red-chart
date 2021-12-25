# `node-red ⚙`

![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)
[![Linting and Testing](https://github.com/dirien/node-red-chart/actions/workflows/lint-and-test.yml/badge.svg)](https://github.com/dirien/node-red-chart/actions/workflows/lint-and-test.yml)
[![Artifact Hub](https://img.shields.io/endpoint?url=https://artifacthub.io/badge/repository/node-red)](https://artifacthub.io/packages/search?repo=node-red)
[![SIT](https://img.shields.io/badge/SIT-awesome-blueviolet.svg?style=flat-square)](https://jobs.schwarz)


<img src="https://nodered.org/about/resources/media/node-red-icon-2.png" width="80" height="80">

A Helm chart for Node-Red, a low-code programming for event-driven applications

**Homepage:** <https://nodered.org/>

## Usage

Adding node-red repository Before installing any chart provided by this repository, add the node-red Charts Repository:

```bash
helm repo add node-red https://schwarzit.github.io/node-red-chart/
helm repo update
```

### Installing the Chart

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

### Uninstalling the Chart

To uninstall the `node-red` deployment:

```bash
helm uninstall node-red
```

### Configuring the Chart

See the [README](charts/node-red/README.md) for more detailed information.

## Contributing 🤝

#### Contributing via GitHub

Feel free to join. Checkout the [contributing guide](CONTRIBUTING.md)

#### License

Apache License, Version 2.0

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| [@dirien](https://github.com/dirien) | engin.diri@mail.schwarz | https://jobs.schwarz |