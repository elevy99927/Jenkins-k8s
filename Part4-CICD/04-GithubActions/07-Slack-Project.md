# GitHub Actions Lab — Slack Notification

## Introduction

In this lab, you will connect a GitHub Actions workflow to Slack and send a notification when the workflow runs successfully.

This exercise demonstrates a common DevOps pattern: notifying teams when a CI/CD pipeline completes.

You will learn how to:

- Create a dedicated Slack channel for pipeline alerts
- Create a Slack `Incoming Webhook`
- Store the webhook securely as a GitHub Actions Secret
- Create a dedicated Git branch for the exercise
- Build a GitHub Actions workflow with multiple jobs
- Use `needs` to control job execution order
- Send a Slack notification from GitHub Actions

---

## Main Task

Create a workflow that runs manually or on push, executes two simple jobs, and sends a Slack notification after the build job completes successfully.

Workflow execution order:

```text
test (echo only) → build (echo only) → notify
```

The `notify` job will use the Slack Notify Marketplace Action:

```text
rtCamp/action-slack-notify@v2
```

---

## Step 1 — Create a Slack Channel

Create a dedicated Slack channel for GitHub Actions notifications.

In Slack:

1. Login to Slack [https://slack.com/](https://slack.com/)
2. Create or Use **Workspace**
3. Go to **Channels**
4. Click **Create channel**
5. Name your channel:

```bash
#elevy99927-alerts
```

This channel will receive notifications from GitHub Actions.

---

## Step 2 — Create a Slack App

Open the Slack Apps page:

```text
https://api.slack.com/apps
```

Then:

1. Click **Create New App**
2. Select **From scratch**
3. App name:

```text
github-actions-bot
```

4. Select your Slack workspace
5. Click **Create App**

---

## Step 3 — Enable Incoming Webhooks

Inside the Slack App:

1. Go to **Features**
2. Select **Incoming Webhooks**
3. Turn on:

```text
Activate Incoming Webhooks
```

This allows Slack to generate a webhook URL that GitHub Actions can use to send messages.

---

## Step 4 — Create the Webhook Token

In the same **Incoming Webhooks** page:

1. Click **Add New Webhook to Workspace**
2. Select the channel:

```text
#elevy99927-alerts
```

3. Click **Allow**
4. Copy the generated Webhook URL

The URL will look similar to:

```text
https://hooks.slack.com/services/XXX/YYY/ZZZ
```

This URL is the Slack webhook token.

Do not commit it to Git.
Do not paste it inside the workflow YAML.
It must be stored as a GitHub Secret.

---

## Step 5 — Create GitHub Secret

In your GitHub repository:

```text
Repository → Settings → Secrets and variables → Actions → Secrets → New repository secret
```

Create the following secret:

```text
SLACK_WEBHOOK
```

Value:

```text
https://hooks.slack.com/services/XXX/YYY/ZZZ
```


---
### Solution

[Slack Notification](./07-Slack-Project.md)