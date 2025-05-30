This repository contains the chart to deploy the client side of the app in a kubernetes cluster in local by using programms like minikube

### Steps

This project uses [helmfile](https://helmfile.readthedocs.io/en/latest/), so make sure that it is installed and create a ```helmfile.yaml``` file with the following lines:

```
releases:
  - name: client
    namespace: frontend
    createNamespace: true
    installed: true
    chart: ./client
    values:
    - ./client/values.yaml
```

Then execute the command to install the chart:

```
helmfile sync
```

Before yo finish, delete the chart installed:

```
helmfile destroy
```
