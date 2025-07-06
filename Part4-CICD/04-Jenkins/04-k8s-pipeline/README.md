# Jenkins Kubernetes Pipeline

## 1. What are PodTemplates?

**PodTemplate** is a Jenkins Kubernetes plugin feature that defines how Jenkins agents run as Kubernetes pods.

**Key Concepts:**
- **Dynamic Agents**: Creates pods on-demand for pipeline execution
- **Container Templates**: Define different containers within the same pod
- **Resource Management**: Automatic cleanup after job completion
- **Isolation**: Each build runs in its own isolated environment

**Basic Structure:**
```groovy
podTemplate(containers: [
    containerTemplate(name: 'container-name', image: 'image:tag', ttyEnabled: true)
]) {
    node(POD_LABEL) {
        // Pipeline steps here
    }
}
```

## 2. Build Advanced Pipeline

### Step 1: Create New Repository

1. **Create GitHub Repository**
   - Go to GitHub and create new repository: `hello-newapp`
   - Initialize with README
   - Clone to local machine:
   ```bash
   git clone https://github.com/YOUR_USERNAME/hello-newapp.git
   cd hello-newapp
   ```

### Step 2: Create Dockerfile and Jenkinsfile

**Create Dockerfile:**
```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

**Create index.html:**
```html
<!DOCTYPE html>
<html>
<head><title>Hello from Jenkins K8s Pipeline</title></head>
<body>
    <h1>Hello World!</h1>
    <p>Built with Jenkins on Kubernetes</p>
</body>
</html>
```

**Create Jenkinsfile:**
```groovy
pipeline {
    agent {
        kubernetes {
            yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: kaniko
    image: gcr.io/kaniko-project/executor:debug
    command:
    - /busybox/cat
    tty: true
    volumeMounts:
    - name: docker-config
      mountPath: /kaniko/.docker
  volumes:
  - name: docker-config
    configMap:
      name: docker-cred
"""
        }
    }
    
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World from SCM Pipeline!'
            }
        }
    }
}
```

**Push to Repository:**
```bash
git add .
git commit -m "Add Dockerfile and Jenkinsfile"
git push origin main
```

### Step 3: Create Jenkins Pipeline from SCM

1. **Create New Pipeline Job**
   - Dashboard → New Item → Pipeline
   - Name: `k8s-pipeline-scm`

2. **Configure Pipeline from SCM**
   - Pipeline Definition: **"Pipeline script from SCM"**
   - SCM: **Git**
   - Repository URL: `https://github.com/YOUR_USERNAME/hello-newapp.git`
   - Branch: `*/main`
   - Script Path: `Jenkinsfile`

3. **Save and Build**
   - Click "Save"
   - Click "Build Now"

## 3. Advanced Pipeline Steps

### Docker Registry Secret (config.json)

**The config.json contains Docker registry authentication:**
```json
{
    "auths": {
        "https://index.docker.io/v1/": {
            "auth": "base64-encoded-username:password"
        }
    }
}
```

**Create Kubernetes ConfigMap:**
```bash
kubectl create configmap docker-cred --from-file=config.json
```

### Complete Advanced Jenkinsfile

```groovy
def appname = "hello-k8s"
def repo = "YOUR_DOCKERHUB_USERNAME"
def appimage = "docker.io/${repo}/${appname}"
def apptag = "${env.BUILD_NUMBER}"

pipeline {
    agent {
        kubernetes {
            yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: kaniko
    image: gcr.io/kaniko-project/executor:debug
    command:
    - /busybox/cat
    tty: true
    volumeMounts:
    - name: docker-config
      mountPath: /kaniko/.docker
  volumes:
  - name: docker-config
    configMap:
      name: docker-cred
"""
        }
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
                sh 'ls -la'
            }
        }
        
        stage('Build with Kaniko') {
            steps {
                container('kaniko') {
                    echo 'Building Docker image with Kaniko...'
                    sh """
                        /kaniko/executor \\
                        --dockerfile=Dockerfile \\
                        --context=. \\
                        --destination=${appimage}:${apptag} \\
                        --destination=${appimage}:latest
                    """
                }
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                echo "Image: ${appimage}:${apptag}"
                echo 'Deployment completed successfully!'
                // Add actual deployment commands here
                // kubectl apply -f deployment.yaml
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline completed!'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
```

### Pipeline Stages Explained:

1. **Checkout**: Downloads source code from SCM repository
2. **Build with Kaniko**: Uses Kaniko to build Docker image without Docker daemon
3. **Deploy**: Placeholder for deployment logic (kubectl commands)

### Key Features:
- **Kaniko**: Builds Docker images inside Kubernetes without Docker daemon
- **ConfigMap**: Stores Docker registry credentials securely
- **Dynamic Pods**: Creates build environment on-demand
- **SCM Integration**: Automatically triggers on code changes

## Troubleshooting

### Error: "couldn't find remote ref refs/heads/master"

**Problem**: Jenkins is looking for `master` branch but your repository uses `main`.

**Solution Options:**

1. **Fix Branch Configuration in Jenkins:**
   - Go to your pipeline configuration
   - Under "Branches to build", change from `*/master` to `*/main`
   - Save and rebuild

2. **Check Your Repository Default Branch:**
   ```bash
   git branch -a
   # Should show: remotes/origin/main
   ```

3. **Alternative: Create master branch (not recommended):**
   ```bash
   git checkout -b master
   git push origin master
   ```

**Best Practice**: Always use `*/main` for new repositories as GitHub changed the default branch name from `master` to `main`.

### Error: "No such property: appimage for class: groovy.lang.Binding"

**Problem**: You're using the simple Jenkinsfile but the pipeline is trying to access variables from the advanced version.

**Solution**: Update your Jenkinsfile in the repository with the complete version:

```groovy
def appname = "hello-k8s"
def repo = "elevy99927"  // Replace with your DockerHub username
def appimage = "docker.io/${repo}/${appname}"
def apptag = "${env.BUILD_NUMBER}"

pipeline {
    agent {
        kubernetes {
            yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: kaniko
    image: gcr.io/kaniko-project/executor:debug
    command:
    - /busybox/cat
    tty: true
    volumeMounts:
    - name: docker-config
      mountPath: /kaniko/.docker
  volumes:
  - name: docker-config
    configMap:
      name: docker-cred
"""
        }
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
                sh 'ls -la'
            }
        }
        
        stage('Build with Kaniko') {
            steps {
                container('kaniko') {
                    echo 'Building Docker image with Kaniko...'
                    echo "Image will be: ${appimage}:${apptag}"
                    // Uncomment when ready to build:
                    // sh """
                    //     /kaniko/executor \\
                    //     --dockerfile=Dockerfile \\
                    //     --context=. \\
                    //     --destination=${appimage}:${apptag} \\
                    //     --destination=${appimage}:latest
                    // """
                }
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                echo "Image: ${appimage}:${apptag}"
                echo 'Deployment completed successfully!'
            }
        }
    }
}
```

**Steps to Fix:**
1. Replace the Jenkinsfile content in your repository
2. Commit and push changes
3. Rebuild the pipeline