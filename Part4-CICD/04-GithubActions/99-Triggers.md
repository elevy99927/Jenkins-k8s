# Workflow Triggers

## Common Event Categories

GitHub Actions supports over 30 distinct event triggers, which generally fall into five core buckets:

| Trigger Category | Primary Events | Common Use Case |
|---|---|---|
| **Code Collaboration** | `push`, `pull_request`, `pull_request_target`, `merge_group` | Running CI tests, linting code, and checking test coverage. |
| **Manual Execution** | `workflow_dispatch`, `repository_dispatch` | Triggering deployments on-demand or responding to external webhooks. |
| **Project Management** | `issues`, `issue_comment`, `discussion`, `label`, `milestone` | Automating issue triage, auto-assigning reviewers, or adding labels. |
| **Automation & DevOps** | `release`, `deployment`, `registry_package`, `page_build` | Deploying a release, publishing a Docker image, or building GitHub Pages. |
| **Automation Schedules** | `schedule` | Running routine maintenance tasks or generating daily backups. |

Full reference: [Events that trigger workflows](https://docs.github.com/en/actions/reference/events-that-trigger-workflows)

---

- [Back to Example](./02-Example.md)
- [Back to GitHub Actions](./README.md)
