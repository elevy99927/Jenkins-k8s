# Install Jenkins

## Add repo

`
helm repo add jenkinsci https://charts.jenkins.io/
helm install my-jenkins jenkinsci/jenkins --version 5.0.17
`

1. Get your 'admin' user password by running:
  kubectl exec --namespace jenkins -it svc/my-jenkins -c jenkins -- /bin/cat /run/secrets/additional/chart-admin-password && echo
2. Get the Jenkins URL to visit by running these commands in the same shell:
  echo http://127.0.0.1:8080
  kubectl --namespace jenkins port-forward svc/my-jenkins 8080:8080



