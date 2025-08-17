#kubectl port-forward svc/grafana 8080:3000 &



kubectl port-forward svc/prometheus-server 8088:80 &
kubectl port-forward svc/phi3mini 11434:11434 &
kubectl port-forward svc/metrics-ai-bridge 8081:8080 &

kubectl port-forward svc/grafana 8080:3000 &

kubectl port-forward --namespace default svc/prometheus-kube-prometheus-prometheus 9090:9090 &



