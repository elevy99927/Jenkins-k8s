# **ARGOCD**

## Part 5: Advanced Hands-On Lab

### **ApplicationSet**

**What is ApplicationSet?**
ApplicationSet is a controller that extends ArgoCD, enabling you to manage **multiple ArgoCD Application resources dynamically**. Instead of defining dozens of separate `Application` manifests, you can use a single `ApplicationSet` with a generator (like Git, list, or cluster) to produce many applications automatically.

**Why use ApplicationSet?**

* Simplifies management of large-scale, multi-environment deployments
* Supports DRY (Don't Repeat Yourself) principles by templating app definitions
* Useful for GitOps patterns where many environments share similar structures

**Example 1: ApplicationSet with List Generator**

Example repo: [argo-demo-repo @ `example-1-appset`](https://github.com/elevy99927/argo-demo-repo/tree/example-1-appset)

```yaml
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: example-applicationset
  namespace: argocd
spec:
  generators:
    - list:
        elements:
          - cluster: dev
            project: project-1
          - cluster: qa
            project: project-1
  template:
    metadata:
      name: '{{project}}-{{cluster}}'
    spec:
      project: default
      source:
        repoURL: https://github.com/elevy99927/argo-demo-repo.git
        targetRevision: example-1-appset
        path: '{{project}}/k8s-{{cluster}}'
      destination:
        server: https://kubernetes.default.svc
        namespace: '{{project}}-{{cluster}}'
      syncPolicy:
        automated:
          prune: true
          selfHeal: true
```

**Example 2: Dynamic Generator (Git Directories)**

Example repo: [argo-demo-repo @ `example-2-dynamic-generator`](https://github.com/elevy99927/argo-demo-repo/tree/example-2-dynamic-generator)

The list generator above is *static* - every app must be typed in by hand. The Git **directory generator** is *dynamic*: ArgoCD scans the repo and creates one Application per folder matching `systems/*/*` (team × cluster). Add a `systems/team-c/dev/` folder in Git and a new Application appears automatically.

Repo layout (branch `example-2-dynamic-generator`):

```
└── systems
    ├── team-a
    │   ├── dev
    │   │   ├── application-a.yaml
    │   │   └── application-b.yaml
    │   ├── qa
    │   │   ├── application-a.yaml
    │   │   └── application-b.yaml
    │   └── prd
    │       ├── application-a.yaml
    │       └── application-b.yaml
    └── team-b
        ├── dev
        │   ├── application-c.yaml
        │   └── application-d.yaml
        ├── qa
        │   ├── application-c.yaml
        │   └── application-d.yaml 
        └── prd
            ├── application-c.yaml
            └── application-d.yaml
```

```yaml
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: systems-dynamic
  namespace: argocd
spec:
  goTemplate: true
  goTemplateOptions: ["missingkey=error"]
  generators:
    - git:
        repoURL: https://github.com/elevy99927/argo-demo-repo.git
        revision: example-2-dynamic-generator
        directories:
          - path: systems/*/*
  template:
    metadata:
      # .path.segments = [systems, team-a, dev]
      name: '{{index .path.segments 1}}-{{.path.basename}}'   # team-a-dev
    spec:
      project: default
      source:
        repoURL: https://github.com/elevy99927/argo-demo-repo.git
        targetRevision: example-2-dynamic-generator
        path: '{{.path.path}}'            # systems/team-a/dev
      destination:
        server: https://kubernetes.default.svc
        namespace: '{{index .path.segments 1}}-{{.path.basename}}'   # team-a-dev
      syncPolicy:
        automated:
          prune: true
          selfHeal: true
        syncOptions:
          - CreateNamespace=true
```

**Example 3: Helm Repo + GitOps Repo with Values (Multi-Source)**

Moved to its own page: [Real Life Example](./RealLifeExample.md)

---
---
### **ApplicationSet Lab (Lab 5)**
* **Step 1** In the remote repository `argo-demo-repo`, create a new branch named `application`.
* **Step 2** Within that branch, create two folders: `app-1/` and `app-2/`.
* **Step 3** Inside each project folder, create three subfolders: `dev/`, `qa/`, and `prod/`, each containing a simple Kubernetes application YAML (e.g., a Pod or Deployment).

```
├── README.md
├── app-1
│   ├── k8s-dev
│   ├── k8s-qa
│   └── k8s-prd
└── app-2
    ├── k8s-dev
    ├── k8s-qa
    └── k8s-prd
```

**Step 4** For each project (e.g., `app-1-dev`, `app-1-qa`, etc.) Create `ApplicationSet`.
* Assume we are working in QA enviorment.
* Your new `path:` shloud be `path: '{{.project}}/{{.cluster}}'`


### Solution: ###
[ApplicationSet.yaml](https://github.com/elevy99927/Jenkins-k8s/blob/main/Part4-CICD/04-ArgoCD/05-ApplicationSet/applicationSet.yaml)


Define multiple ArgoCD Applications, each targeting one of these environments (e.g., `project-1-dev`, `project-1-qa`, etc.), and manage them through ArgoCD’s UI or Git.



By the end of this lab, students should be able to manage multiple ArgoCD applications, understand the differences between Git-synced apps and Helm-based apps, and modify applications declaratively using Git workflows.

---
---
### **User Managment (Lab 6)**
TBD

---
---
- [Back to Argo Tutorial](./README.md)
- [Basic Labs](./Basic-Labs.md)
- [Real Life Example](./RealLifeExample.md)

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