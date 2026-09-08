# Changelog

## 2026-09-08

### ArgoCD (`Part4-CICD/04-ArgoCD`)
- Advanced-Labs: added **Example 2** – dynamic Git *directory* generator over `systems/<team>/<cluster>` (one Application per folder, no hardcoded list).
- Advanced-Labs: added **Example 3** – Git *files* generator + Helm multi-source: chart from the Helm repo, values from the GitOps repo at `systems/<team>/<cluster>/<namespace>/<app>-values.yaml` (one Application per values file, team/cluster/namespace/app derived from the path).
- Advanced-Labs: each example now links to its branch in [argo-demo-repo](https://github.com/elevy99927/argo-demo-repo): `example-1-appset`, `example-2-dynamic-generator`, `example-3-helm-values`.
- Advanced-Labs: Example 2 cluster folders renamed `k8s-dev/qa/prd` → `dev/qa/prd`.

### n8n (`Part4-CICD/04-N8N`)
- `run-docker.sh`: set `N8N_SECURE_COOKIE=false`, expose port `5679`.
