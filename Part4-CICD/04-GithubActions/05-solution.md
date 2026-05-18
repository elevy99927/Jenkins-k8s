Example workflow:

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

      - name: Install Trivy CLI
        uses: ankurk91/install-trivy-cli-action@v2
        with:
          version: latest
          cache: true

      - name: Verify Trivy installation
        run: trivy --version

      - name: Run Trivy filesystem scan
        run: trivy fs --severity HIGH,CRITICAL --exit-code 1 .
```

Expected result:

- Trivy is installed on the runner
- Repository filesystem is scanned
- Workflow fails if HIGH or CRITICAL vulnerabilities are found

---

Back: [05-Marketplace-Actions.md](./05-Marketplace-Actions.md)
