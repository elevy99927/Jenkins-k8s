
# Install Metrisc Server
``` bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

```


# Install Prometheus

```bash
kubectl create ns monitoring

helm repo add prometheus-community \
  https://prometheus-community.github.io/helm-charts \
  --force-update

helm repo update

helm upgrade --install prometheus \
  prometheus-community/kube-prometheus-stack \
  --version 86.1.0 \
  --namespace monitoring \
  --create-namespace \
  --set grafana.adminPassword=Aa123456 \
  --wait \
  --timeout 10m

```

# Install Loki

```bash
helm repo add grafana https://grafana.github.io/helm-charts --force-update

helm repo update

helm upgrade --install loki \
  grafana/loki \
  --namespace monitoring \
  --create-namespace \
  --set deploymentMode=SingleBinary \
  --set loki.auth_enabled=false \
  --set loki.commonConfig.replication_factor=1 \
  --set loki.storage.type=filesystem \
  --set singleBinary.replicas=1 \
  --set read.replicas=0 \
  --set write.replicas=0 \
  --set backend.replicas=0 \
  --set loki.useTestSchema=true 

```

---
# Install Promtail

```bash
helm upgrade --install promtail \
  grafana/promtail \
  --namespace monitoring \
  --create-namespace \
  --set config.lokiAddress=http://loki:3100/loki/api/v1/push
```

---


## Fix for AWS 
**ONLY IF if you are running on AWS**
```sh
kubectl patch svc prometheus-kube-prometheus-prometheus -n monitoring -p '{"spec": {"type": "LoadBalancer"}}'
kubectl patch svc rometheus-grafana -n monitoring -p '{"spec": {"type": "LoadBalancer"}}'

```
---





# Cleanup
```bash
helm uninstall promtail -n monitoring
helm uninstall loki -n monitoring
helm uninstall prometheus
kubectl delete mutatingwebhookconfiguration \
  prometheus-kube-prometheus-admission \
  --ignore-not-found

kubectl delete validatingwebhookconfiguration \
  prometheus-kube-prometheus-admission \
  --ignore-not-found

kubectl delete job \
  prometheus-kube-prometheus-admission-create \
  prometheus-kube-prometheus-admission-patch \
  --ignore-not-found

  ```

