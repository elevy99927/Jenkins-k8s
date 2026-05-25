
# Slack Lab Solution

Add the following workflow to:

```text
.github/workflows/slack-notification.yaml
```

```yaml
name: slack-notification-demo

on:
  workflow_dispatch:
  push:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - run: echo "running tests"

  build:
    runs-on: ubuntu-latest
    needs: test

    steps:
      - run: echo "building app"

  notify:
    runs-on: ubuntu-latest
    needs: build

    steps:
      - name: Send Slack notification
        uses: rtCamp/action-slack-notify@v2
        env:
          SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK }}
          SLACK_CHANNEL: elevy99927-alerts
          SLACK_USERNAME: elevy
          SLACK_TITLE: GitHub Actions Notification
          SLACK_MESSAGE: "Workflow executed successfully"
          SLACK_COLOR: good
```

---

## Commit and Push

```bash
git add .github/workflows/slack-notification.yaml
git commit -m "add slack notification workflow"
git push origin slack
```

---

## Run the Workflow

You can run this workflow in two ways.

### Option 1 — Manual Run

In GitHub:

```text
Repository → Actions → slack-notification-demo → Run workflow
```

### Option 2 — Push Trigger

Push a new commit to the branch:

```bash
git commit --allow-empty -m "trigger slack workflow"
git push origin slack
```

---

## Expected Result

The workflow should run in this order:

```text
test → build → notify
```

Expected GitHub Actions logs:

```text
running tests
building app
```

Expected Slack result:

A message appears in:

```text
#elevy99927-alerts
```

Message:

```text
Workflow executed successfully
```

---

# Explanation

## `workflow_dispatch`

Allows manual workflow execution from the GitHub Actions UI.

```yaml
on:
  workflow_dispatch:
```

## `push`

Runs the workflow automatically when code is pushed.

```yaml
on:
  push:
```

## `needs`

Controls job dependency order.

```yaml
needs: test
```

Means:

```text
build depends on test
```

In this workflow:

```yaml
build:
  needs: test

notify:
  needs: build
```

Execution order:

```text
test → build → notify
```

## `SLACK_WEBHOOK`

The Slack webhook URL is stored securely as a GitHub Actions Secret.

```yaml
SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK }}
```

This prevents exposing the webhook URL in the repository.

---

Back: [07-Slack-Project.md](./07-Slack-Project.md)