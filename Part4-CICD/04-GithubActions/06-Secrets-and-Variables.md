# Secrets and Variables


## Technical Background

Secrets securely store credentials.

Variables store non-sensitive configuration.

Never hardcode:

- API keys
- passwords
- cloud credentials

---

## Where We Configure Secrets

GitHub Actions `secrets` can be configured in three main scopes:

| Scope |  When to use |
|---|---|
| Repository Secret |   Secret is used only by one repository |
| Environment Secret |  Secret is specific to an environment such as `dev`, `staging`, or `prod` |
| Organization Secret | Secret should be shared across multiple repositories |

---

## Repository Secret

Use this for most common workflows in Github Actions.

Configuration Path:

```yaml
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

```yaml
Repository → Settings → Environments → production → Environment secrets
```

Example use case:

```text
PROD_API_TOKEN
PROD_KUBECONFIG
```

In the workflow, the job **must** reference the `environment`:

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

```yaml
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


### Part 1

Implement environment-specific variables. 
- Create repository variable named `MY_ENVIORMENT` for enviorment `production` and for `development`
- Print `MY_ENVIORMENT` for `environment: production`

### Part 2
- Create repository secret named `JB_DEMO_USER`
- Use this Secret and print it in your solution 





