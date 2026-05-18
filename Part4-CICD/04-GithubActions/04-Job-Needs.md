# Part 2 — Jobs, Steps and Events

## Technical Background

Workflows are composed of jobs.

Jobs can:

- run independently
- run sequentially
- depend on each other

GitHub Actions executes jobs on isolated runners.

---

## Example

```yaml
name: ci

on:
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
```

---

## `needs` Meaning

`needs: test` means that the current job depends on the job named `test`.

In simple words:

```text
build depends on test
```

Execution order:

```text
test → build
```

Without `needs`, jobs run in parallel by default.

With `needs: test`, the `build` job starts only after the `test` job completes successfully.

If `test` fails, `build` will not run.

---

## Basic Exercise

Create:

- test job
- build job
- sequential execution using `needs`

---

## Advanced Exercise

Implement:

- push trigger for main
- pull_request trigger
- separate behavior per branch

