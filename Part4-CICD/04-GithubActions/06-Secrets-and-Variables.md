# Secrets and Variables


## Technical Background

Secrets securely store credentials.

Variables store non-sensitive configuration.

Never hardcode:

- API keys
- passwords
- cloud credentials

---

## Where to Configure Secrets

GitHub Actions secrets can be configured in three main scopes:

| Scope | Where to configure | When to use |
|---|---|---|
| Repository Secret | Repository → Settings → Secrets and variables → Actions → Secrets | Secret is used only by one repository |
| Environment Secret | Repository → Settings → Environments → Select environment → Environment secrets | Secret is specific to an environment such as `dev`, `staging`, or `prod` |
| Organization Secret | Organization → Settings → Secrets and variables → Actions → Secrets | Secret should be shared across multiple repositories |

---

## Repository Secret

Use this for most beginner workflows.

Path:

```text
Repository → Settings → Secrets and variables → Actions → Secrets → New repository secret
```

Example use case:

```text
DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
API_TOKEN
```

---

## Environment Secret

Use this when the same workflow deploys to different environments.

Path:

```text
Repository → Settings → Environments → production → Environment secrets
```

Example use case:

```text
PROD_API_TOKEN
PROD_KUBECONFIG
```

In the workflow, the job must reference the environment:

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production

    steps:
      - run: echo "Deploying to production"
```

---

## Organization Secret

Use this when many repositories need the same secret.

Path:

```text
Organization → Settings → Secrets and variables → Actions → Secrets → New organization secret
```

Example use case:

```text
SHARED_DOCKERHUB_TOKEN
ORG_NPM_TOKEN
```

Organization secrets can be limited to selected repositories.

---

## Example

```yaml
env:
  APP_ENV: production

steps:
  - run: echo $APP_ENV
```

```yaml
env:
  TOKEN: ${{ secrets.API_TOKEN }}
```

---

## Basic Exercise

Create repository secret and use it.

---

## Advanced Exercise

Implement:

Environment-specific variables. For example: Differant vers for branch `main` and for branch `dev`


