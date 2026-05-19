
# Introduction to GitHub Actions

## Technical Background

GitHub Actions is GitHub’s native CI/CD automation platform.

It allows developers and DevOps engineers to automate software workflows directly from a GitHub repository.

Typical automation flows include:

- Running tests
- Building applications
- Security scanning (e.g. SAST)
- Packaging artifacts 
- Deploying applications


GitHub Actions workflows are defined using YAML files located under:

```bash
.github/workflows/
```

---

## Why GitHub Actions Matters

**Modern software teams aim to:**

- reduce manual work
- improve delivery speed
- detect issues earlier
- standardize deployments
- improve reliability

**Without CI/CD:**

- deployments become manual -> limit release velocity
- bugs reach production more often
- environments drift
- delivery becomes slow and error-prone

GitHub Actions helps solve these issues through automation.

---

## Core Concepts

| Component | Description |
|---|---|
| Workflow | YAML automation definition |
| Event | Trigger for workflow execution |
| Job | Group of execution steps |
| Step | Single command or action |
| Runner | Machine executing the workflow |
| Action | Reusable automation component (TBD)|

---
## Hierarchy
```
Workflow
 ├── Job
 │    ├── Step
 │    ├── Step
 │    └── Step
 │
 └── Job
      ├── Step
      └── Step
```
---
## Workflow Execution Flow

```text
Git Event
   ↓
Workflow Triggered
   ↓
Runner Starts
   ↓
Jobs Execute
   ↓
Steps Execute
   ↓
Result + Logs
```

---

## GitHub Runners

GitHub provides [managed runners](https://docs.github.com/en/actions/concepts/runners/github-hosted-runners):

GitHub offers hosted virtual machines to run workflows. The virtual machine contains an environment of tools, packages, and settings available for GitHub Actions to use.

- Ubuntu
- Windows
- macOS

Runner Example:

```yaml
runs-on: ubuntu-latest
```

The runner is a temporary VM/container that executes the workflow.

---
