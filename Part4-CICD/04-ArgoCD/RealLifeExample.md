# **ARGOCD**

## Real Life Example: Helm Repo + GitOps Repo with Values (Multi-Source)

Example repo: [argo-demo-repo @ `example-3-helm-values`](https://github.com/elevy99927/argo-demo-repo/tree/example-3-helm-values)

*** Real Production Example ***
The chart comes from a **Helm repository**, the values come from your **GitOps repository**. This uses ArgoCD *multi-source* apps: the Git source is given a `ref: values`, and the Helm source references it with `$values/...`.

Nothing is hardcoded. The Git **files generator** scans `systems/*/*/*/*-values.yaml` and creates **one Application per values file**. The path encodes everything:

```
systems/<team>/<cluster>/<namespace>/<app>-values.yaml
```

Add a new team, cluster, namespace or app in Git → a new Application appears. Delete the file → the Application is removed.

Repo layout (branch `example-3-helm-values`):

```
└── systems
    ├── team-a
    │   ├── k8s-dev
    │   │   ├── frontend-ns
    │   │   │   ├── fe-a-values.yaml
    │   │   │   └── fe-b-values.yaml
    │   │   └── backend-ns
    │   │       └── be-c-values.yaml
    │   ├── k8s-qa
    │   │   ├── frontend-ns
    │   │   │   ├── fe-a-values.yaml
    │   │   │   └── fe-b-values.yaml
    │   │   └── backend-ns
    │   │       └── be-c-values.yaml
    │   └── k8s-prd
    │       ├── frontend-ns
    │       │   ├── fe-a-values.yaml
    │       │   └── fe-b-values.yaml
    │       └── backend-ns
    │           └── be-c-values.yaml
    └── team-b
        ├── k8s-dev
        │   └── payments-ns
        │       ├── payment-d-values.yaml
        │       └── payment-e-values.yaml
        ├── k8s-qa
        │   └── payments-ns
        │       ├── payment-d-values.yaml
        │       └── payment-e-values.yaml
        └── k8s-prd
            └── payments-ns
                ├── payment-d-values.yaml
                └── payment-e-values.yaml
```

Example `systems/team-a/k8s-dev/frontend-ns/application-a-values.yaml` (podinfo chart values):

```yaml
replicaCount: 1
ui:
  message: "application-a | team-a | k8s-dev | frontend-ns"
```

```yaml
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: systems-helm
  namespace: argocd
spec:
  goTemplate: true
  goTemplateOptions: ["missingkey=error"]
  generators:
    - git:
        repoURL: https://github.com/elevy99927/argo-demo-repo.git
        revision: example-3-helm-values
        files:
          - path: "systems/*/qa/*/*-values.yaml"
  # For every matched file:
  #   .path.path     = systems/team-a/dev/frontend-ns
  #   .path.segments = [systems, team-a, dev, frontend-ns]
  #   .path.filename = app-a-values.yaml
  template:
    metadata:
      # team-a-dev-frontend-ns-app-a
      name: '{{index .path.segments 1}}-{{index .path.segments 2}}-{{index .path.segments 3}}-{{.path.filename | trimSuffix "-values.yaml"}}'
      labels:
        team: '{{index .path.segments 1}}'
        cluster: '{{index .path.segments 2}}'
        app: '{{.path.filename | trimSuffix "-values.yaml"}}'
    spec:
      project: default
      sources:
        # 1. Chart from the Helm repo
        - repoURL: https://stefanprodan.github.io/podinfo
          chart: podinfo
          targetRevision: 6.5.0
          helm:
            releaseName: '{{.path.filename | trimSuffix "-values.yaml"}}'
            valueFiles:
              - $values/{{.path.path}}/{{.path.filename}}
        # 2. Values from the GitOps repo
        - repoURL: https://github.com/elevy99927/argo-demo-repo.git
          targetRevision: example-3-helm-values
          ref: values
      destination:
        # cluster folder name == cluster name registered in ArgoCD
        # (argocd cluster add <kube-context> --name dev)
        # single-cluster lab: replace with  server: https://kubernetes.default.svc
        server: https://kubernetes.default.svc
        namespace: '{{index .path.segments 3}}'
      syncPolicy:
        automated:
          prune: true
          selfHeal: true
        syncOptions:
          - CreateNamespace=true

```

---
---
- [Back to Argo Tutorial](./README.md)
- [Basic Labs](./Basic-Labs.md)
- [Advanced Labs](./Advanced-Labs.md)

---
---
## Contact

For questions or feedback, feel free to reach out:

- **Email**: eyal@levys.co.il
- **GitHub**: [https://github.com/elevy99927](https://github.com/elevy99927)
