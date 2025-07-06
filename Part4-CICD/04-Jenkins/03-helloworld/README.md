# Jenkins Pipeline: Hello World

## Declarative vs Scripted Pipeline

### Declarative Pipeline
- **Structure**: Uses predefined structure with `pipeline {}` block
- **Syntax**: More readable and structured
- **Error Handling**: Built-in validation and error handling
- **Best Practice**: Recommended for most use cases

```groovy
pipeline {
    agent any
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World!'
            }
        }
    }
}
```

### Scripted Pipeline
- **Structure**: Uses Groovy scripting with `node {}` block
- **Syntax**: More flexible but complex
- **Control**: Full programmatic control
- **Use Case**: Advanced scenarios requiring complex logic

```groovy
node {
    stage('Hello') {
        echo 'Hello World!'
    }
}
```
### Key Differences Summary

| Feature         | Declarative              | Scripted                 |
| --------------- | ------------------------ | ------------------------ |
| Style           | Declarative (What to do) | Procedural (How to do)   |
| Structure       | Strict and well-defined  | Flexible and open        |
| Learning Curve  | Easier                   | Steeper                  |
| Validation      | Automatic                | Manual                   |
| Flexibility     | Limited                  | Full                     |
| Recommended For | Standard use cases       | Advanced logic scenarios |

### When to Use What?

* **Declarative** pipelines are perfect when you want to set up a straightforward CI/CD flow: build, test, deploy.
* **Scripted** pipelines are best when you need loops, conditionals, or integration with custom logic (like reading a file or dynamic branching).

---

## Hands-On: Create Hello World Job

### Step 1: Create New Pipeline Job
1. Go to Jenkins Dashboard
2. Click **"New Item"**
3. Enter name: `hello-world-pipeline`
4. Select **"Pipeline"**
5. Click **"OK"**

### Step 2: Configure Pipeline Script

**Option A: Declarative Pipeline**
```groovy
pipeline {
    agent any
    stages {
        stage('Greeting') {
            steps {
                echo 'Hello World from Declarative Pipeline!'
                echo "Build Number: ${env.BUILD_NUMBER}"
                echo "Job Name: ${env.JOB_NAME}"
            }
        }
        stage('Environment Info') {
            steps {
                sh 'date'
                sh 'whoami'
            }
        }
    }
}
```

**Option B: Scripted Pipeline**
`hello-world-scripted-pipeline`
```groovy
node {
    stage('Greeting') {
        echo 'Hello World from Scripted Pipeline!'
        echo "Build Number: ${env.BUILD_NUMBER}"
        echo "Job Name: ${env.JOB_NAME}"
    }
    
    stage('Environment Info') {
        sh 'date'
        sh 'whoami'
    }
}
```

### Step 3: Run the Pipeline
1. Click **"Save"**
2. Click **"Build Now"**
3. Check **"Console Output"** to see results

### Expected Output
```
Started by user admin
Running in Durability level: MAX_SURVIVABILITY
[Pipeline] Start of Pipeline
[Pipeline] node
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Greeting)
[Pipeline] echo
Hello World from Scripted Pipeline!
[Pipeline] echo
Build Number: 1
[Pipeline] echo
Job Name: hello-world-pipeline
[Pipeline] }
[Pipeline] stage
[Pipeline] { (Environment Info)
[Pipeline] sh
+ date
Mon Jan 15 10:30:45 UTC 2024
[Pipeline] sh
+ whoami
jenkins
[Pipeline] }
[Pipeline] }
[Pipeline] End of Pipeline
Finished: SUCCESS
```

## Key Differences Summary

| Feature | Declarative | Scripted |
|---------|-------------|----------|
| Syntax | Structured | Flexible |
| Learning Curve | Easier | Steeper |
| Validation | Built-in | Manual |
| Recommended | Yes | Advanced use |