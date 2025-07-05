# Jenkins Installation with Helm

## Prerequisites
- Kubernetes cluster running
- Helm 3.x installed
- kubectl configured to access your cluster

## Installation Steps

### 1. Add Jenkins Helm Repository
```bash
helm repo add jenkinsci https://charts.jenkins.io
helm repo update
```
---

### 2. Install Jenkins
```bash
helm install jenkins jenkinsci/jenkins
```

### 2.1. Check Installation Status
```bash
kubectl get pods --namespace default -l "app.kubernetes.io/instance=jenkins"
helm status jenkins
```
Wait for the pod to be in "Running" state before proceeding.

---

### 3. Get Admin Password
```bash
kubectl exec --namespace default -it svc/jenkins -c jenkins -- /bin/cat /run/secrets/additional/chart-admin-password && echo
```
**KEEP YOUR ADMIN PASSWORD!!**

---

### 4. Access Jenkins

#### Option 1: Google Cloud Shell (Port Forward)
```bash
kubectl --namespace default port-forward svc/jenkins 8080:8080
```
Then open http://localhost:8080 in your browser.

#### Option 2: AWS (Service Access)

**LoadBalancer (Recommended for Production)**
```bash
kubectl get svc jenkins --namespace default
```
Use the EXTERNAL-IP from the LoadBalancer service to access Jenkins.
- **Pros**: Automatic external IP, built-in load balancing
- **Cons**: Costs money, requires cloud provider support

**NodePort (Alternative)**
```bash
kubectl get nodes -o wide
kubectl get svc jenkins --namespace default
```
Access via `<NODE-IP>:<NODE-PORT>`
- **Pros**: Free, works on any Kubernetes cluster
- **Cons**: Manual port management, less secure

**Required Ports:**
- **8080**: Jenkins web UI
- **50000**: Jenkins agent communication (JNLP)


## Configuration Options

For custom configuration, see [VALUES.md](./VALUES.md) for common examples:
```bash
helm install jenkins jenkinsci/jenkins -f values.yaml
```

## Useful Commands

- **Upgrade**: `helm upgrade jenkins jenkinsci/jenkins`
- **Uninstall**: `helm uninstall jenkins`
- **Status**: `helm status jenkins`

For more details, visit: https://artifacthub.io/packages/helm/jenkinsci/jenkins

---
### 5. Work with Jenkins

**Login**
use the admin password from [Step 3](https://github.com/elevy99927/Jenkins-k8s/tree/main/Part4-CICD/04-Jenkins/01-install#3-get-admin-password)

<img src="./images/login.png" border="1">

---
**Welcome to Jenkins!**
<img src="./images/welcome.png" border="1">


---
### **Next Steps**
<A href="../02-manage/README.md">Manage Jenkins</A>