# Marketplace Actions

## Technical Background

GitHub Marketplace provides reusable actions.

Actions reduce duplicated logic and standardize automation.

**Common actions:**

- checkout
- setup-python
- setup-node
- cache
- docker actions


## Marketplace Link

GitHub Actions Marketplace:

https://github.com/marketplace?type=actions


## Example

```yaml
steps:
  - uses: actions/checkout@v4

  - uses: actions/setup-python@v5
    with:
      python-version: "3.12"
```

This example shows two common Marketplace Actions used in many CI pipelines.

### `actions/checkout@v4`

```yaml
- uses: actions/checkout@v4
```
This action downloads the repository source code into the runner.


### `actions/setup-python@v5`

```yaml
- uses: actions/setup-python@v5
  with:
    python-version: "3.12"
```

This action installs and configures `Python 3.12 `on the runner.

### Runnins our Actions

To run the action we will use the `run` method:

```yaml
run:
```

Real CI pipelines example:

```yaml
steps:
  - uses: actions/checkout@v4

  - uses: actions/setup-python@v5
    with:
      python-version: "3.12"

  - run: pip install -r requirements.txt

  - run: pytest
```


## Simple Lab — Hello World JS Action

**Source:**

https://github.com/marketplace/actions/hello-world-js-action

**Objective:**

Run a simple third-party Marketplace Action and pass input to it.

### Walk through example:

```yaml
name: marketplace-hello-world

on:
  push:
  workflow_dispatch:

jobs:
  hello-world:
    runs-on: ubuntu-latest

    steps:
      - name: Run Hello World JS Action
        uses: actions/hello-world-javascript-action@main
        with:
          who-to-greet: "GitHub Actions Student"
```

Expected result:
- push will run automaticly 
- The action prints a greeting in the workflow logs

**NOTE**
- Workflow runs manually from the Actions tab


## Advanced Exercise

Add:

- dependency cache
- custom action inputs

## Advanced Lab — Install Trivy CLI and Run Scan

### Duration

30 minutes

### Source:

https://github.com/marketplace/actions/install-trivy-cli

### Objective:

- Install Trivy CLI from a Marketplace Action and run a vulnerability scan.
- Print Trivy version
- Iscan the code with Trivy

### LAB Trivy scan with actions

```yaml
name: trivy-scan

on:
  workflow_dispatch:

jobs:
  scan:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

        ### Add Your solution hare...
```

Expected result:

- Trivy is installed on the runner
- Repository filesystem is scanned
- Workflow fails if HIGH or CRITICAL vulnerabilities are found

### Solution

[Marketplace Actions Solution](./05-Marketplace-Actions.md)
