
# Example Workflow

```yaml
name: hello-actions

on:
  push:

jobs:
  hello:
    runs-on: ubuntu-latest #free tier - 2,000 minutes per month

    steps:
      - name: Print message
        run: echo "Hello GitHub Actions"
```

---

# YAML Breakdown

## Workflow Name

```yaml
name: hello-actions
```

Human-readable workflow name.

---

## Trigger

```yaml
on:
  push:
```

Execute workflow when code is pushed to the git repo.

More trigger examples:

```yaml
on:
  pull_request:

  push:
    branches:
      - main
      - fb-demo

  workflow_dispatch:
```

---

## Job Definition

```yaml
jobs:
```

Container for all jobs.

---

## Runner

```yaml
runs-on: ubuntu-latest
```

Defines execution environment.

---

## Step

```yaml
steps:
  ...
```

List of commands/actions to execute.

---

## Command Execution

```yaml
run: echo "Hello GitHub Actions"
```

Executes shell command.


