# **ARGOCD**

## Part 3: Hands-On Lab

### Lab Overview ###

This hands-on lab is designed to provide students with practical experience using ArgoCD for both GitOps-style synchronization from their own repositories and direct deployment of Helm charts from remote sources. The lab is divided into basic and advanced sections to gradually build up capabilities.

---

### LAB 1. ###
Create a personal GitHub repository containing Kubernetes manifests, connect it to ArgoCD, and synchronize it as an ArgoCD Application.
* **Task 1:** Create Project in ArgoCD using the `AppProject` CRD.
* **Task 2:** Create application in ArgoCD using the `Application` CRD.
* **Project Name:** `my-project`
* **Application Name:** `demo-app`
* **Example Yaml:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: color-deploy
spec:
  selector:
    matchLabels:
      app: color
  replicas: 1
  template:
    metadata:
      labels:
        app: color
    spec:
      containers:
      - name: color
        image: elevy99927/color:red
        ports:
        - containerPort: 80

```
* **Hints:**
* [AppProject Example](https://github.com/elevy99927/Jenkins-k8s/blob/main/Part4-CICD/04-ArgoCD/01-simpleapp/project.yaml)
* [Application Example](https://github.com/elevy99927/Jenkins-k8s/blob/main/Part4-CICD/04-ArgoCD/01-simpleapp/application.yaml)
* [Argo Demo App](https://github.com/elevy99927/argo-demo-repo/tree/main) - You can clone this repo.

---

### Lab 2: ###
Deploy the `podinfo` Helm chart (version `6.5.0`) using ArgoCD with no need to manage the chart source locally.
* The only referance you have is this link:
<BR>[Artifact hub](https://artifacthub.io/packages/helm/podinfo/podinfo?modal=install)

* **Task 1:** Create application in ArgoCD using the `Application` CRD.
```yaml
  source:
    repoURL: https://stefanprodan.github.io/podinfo
    chart: podinfo
    targetRevision: 6.5.0
```

* **Hints:**
* [Application Example](https://github.com/elevy99927/Jenkins-k8s/blob/main/Part4-CICD/04-ArgoCD/02-multi-repo/podinfo-app.yaml)
---

### Lab 3: ###
Upgrade the deployed Helm chart to version `6.6.0` by updating the `Application` definition.

---

### **Lab 4:**

This lab demonstrates how to change the Git branch ArgoCD pulls from, simulating real-world scenarios such as promoting changes from dev to prod. It is essential for managing multi-environment pipelines using Git branches.

**TASK 1:** In your application repo in guthub `argo-demo-repo` create a new branch named dev. with a new `deployment.yaml`
**TASK 2:** Modify the ArgoCD Application to switch from the `main` branch to a `dev` branch.

**Hint:**

```yaml
  source:
    repoURL: https://github.com/elevy99927/argo-demo-repo.git
    ## add pull from branch dev
    targetRevision: dev
    path: .
```

**Solution:**
[Lab 4 Solution - application.yaml](https://github.com/elevy99927/Jenkins-k8s/blob/main/Part4-CICD/04-ArgoCD/04-multi-branch/application.yaml)

---
---
- [Back to Argo Tutorial](./README.md)
- [Advanced Labes](./Advanced-Labs.md)

---
---
## Open in Google Cloud Shell

You can directly open this repository in Google Cloud Shell to start exploring the examples:

[![Open in Google Cloud Shell](https://camo.githubusercontent.com/198b1d237c4023111c3f163552130daf552a0a684ea7a8ed1adc98c9b7f59659/68747470733a2f2f677374617469632e636f6d2f636c6f75647373682f696d616765732f6f70656e2d62746e2e737667)](https://shell.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/elevy99927/Jenkins-k8s)


---
---
## Contact

For questions or feedback, feel free to reach out:

- **Email**: eyal@levys.co.il
- **GitHub**: [https://github.com/elevy99927](https://github.com/elevy99927)