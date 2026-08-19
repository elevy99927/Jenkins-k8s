## Install kubeapps

```bash
# Apply CRDs
kubectl apply -f apprepository-crd.yaml

# install kubeapps
kubectl apply -f kubeapps-all-in-one.yaml

```

### Wait for all pods to be Running:

```bash
kubectl get pods -n kubeapps -w
```

### Open the dashboard:

```bash
kubectl port-forward -n kubeapps svc/kubeapps 8080:80
```
then visit <a href="http://localhost:8080">http://localhost:8080</a>


## Log in
Kubeapps has no built-in admin/password; it authenticates with a Kubernetes API token tied to a ServiceAccount/RBAC. Create one and get its token:

```
kubectl create serviceaccount kubeapps-admin -n kubeapps
kubectl create clusterrolebinding kubeapps-admin --clusterrole=cluster-admin --serviceaccount=kubeapps:kubeapps-admin
kubectl create token kubeapps-admin -n kubeapps
```
Paste that token into the Kubeapps login screen.


