
# Using Kaniko

Kaniko is preferred over Docker-in-Docker (DinD) primarily because it allows you to build container images securely and efficiently without requiring root privileges or a running Docker daemon

## Advanced Pipeline with Kaniko Steps

### Docker Registry Secret (config.json)

The `config.json` contains Docker registry authentication for Kaniko to push images to Docker Hub. <BR>
For example <A Href="https://hub.docker.com/">https://hub.docker.com</a>

#### Step-by-Step Creation:

**1. Create Base64 Encoded Credentials:**
```bash
# Replace YOUR_USERNAME and YOUR_PASSWORD with actual Docker Hub credentials
echo -n "YOUR_USERNAME:YOUR_PASSWORD" | base64
```

**2. Create config.json file:**
```json
{
    "auths": {
        "https://index.docker.io/v1/": {
            "auth": "YOUR_BASE64_ENCODED_CREDENTIALS_HERE"
        }
    }
}
```

**Example:**
- Username: `myuser`
- Password: `mypassword`
- Command: `echo -n "myuser:mypassword" | base64`
- Result: `bXl1c2VyOm15cGFzc3dvcmQ=`

**Example config.json:**
```json
{
    "auths": {
        "https://index.docker.io/v1/": {
            "auth": "bXl1c2VyOm15cGFzc3dvcmQ="
        }
    }
}
```

**3. Create Kubernetes ConfigMap:**
```bash
kubectl create configmap docker-cred --from-file=config.json
```

**4. Verify ConfigMap:**
```bash
kubectl get configmap docker-cred -o yaml
```

### Complete Advanced Jenkinsfile

```groovy

def appname = "hello-newapp"
def repo = "elevy99927"  // Replace with your DockerHub username
def artifactory = "docker.io" 
def appimage = "docker.io/${repo}/${appname}"
def apptag = "${env.BUILD_NUMBER}"

podTemplate(containers: [
      containerTemplate(name: 'jnlp', image: 'jenkins/inbound-agent', ttyEnabled: true),
      containerTemplate(name: 'docker', image: 'gcr.io/kaniko-project/executor:debug-v0.19.0', command: "/busybox/cat", ttyEnabled: true)
  ],
  volumes: [
     configMapVolume(mountPath: '/kaniko/.docker/', configMapName: 'docker-cred')
  ])  {
    node(POD_LABEL) {
        stage('chackout') {
            container('jnlp') {
            sh '/usr/bin/git config --global http.sslVerify false'
	    checkout scm
          }
        } // end chackout

        stage('build') {
            container('docker') {
              echo "Building docker image..."
	      echo "Original step was using docker for build."
	      echo "You will need to use kaniko instead"
              sh "echo docker build -t $appimage --no-cache ."
              sh "echo docker login $artifactory -u admin -p password"
              sh "echo docker push $appimage"
            }
        } //end build

        stage('deploy') {
            container('docker') {
	      if (DEPLOY) {
                echo "***** Doing some deployment stuff *********"
             }  else {
                echo "***** NO DEPLOY - Doing somthing else. Testing? *********"
             }
           }
        } //end deploy
    }
    /*
    post {
        always {
            echo 'Pipeline completed!'
        }
        success {
            echo 'Pipeline succeeded!'
            echo 'Send sucess email'
            echo 'Notify CMDB'
        }
        failure {
            echo 'Pipeline failed!'
            echo 'send error email'
        }
    }
    */
}
```



# Kaniko Lab:
Based on the `Complete Advanced Jenkinsfile` Do the following steps:
- **Kaniko**: Use [kaniko](https://github.com/GoogleContainerTools/kaniko) to build your image


---
Next Step: [upload your code to github](../05-upload-to-github/)