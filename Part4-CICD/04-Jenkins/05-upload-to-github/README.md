# Upload to GitHub Pipeline

This guide shows how to configure Jenkins to push YAML files back to GitHub after building.

## 1. Create GitHub Token

1. Go to GitHub ->  Settings -> Developer settings -> Personal access tokens ->  Tokens (classic)
2. Click "Generate new token (classic)"
3. Set expiration and select scopes:
   - `repo` (Full control of private repositories)
   - `workflow` (Update GitHub Action workflows)
4. Copy the generated token
---
**Create Token**
<img src="./images/Settings.png">
---

**Set Repository access**

<img src="./images/access.png">

---

**Generate Token**

<img src="./images/generate.png">

---

## 2. Save Token in Jenkins

1. Go to Jenkins → Manage Jenkins → Credentials
2. Click on "System" → "Global credentials"
3. Click "Add Credentials"
4. Select "Username with password"
5. Fill in:
   - Username: Your GitHub username
   - Password: The GitHub token you created
   - ID: `github-credentials`
   - Description: GitHub Token

---

## 3. Pipeline Stage

Add this stage to your Jenkinsfile to push YAML files back to GitHub:

```groovy
stage('push-yaml') {
    container('jnlp') {
        withCredentials([usernamePassword(credentialsId: 'github-credentials', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD')]) {
            sh '''
                git config user.email "jenkins@example.com"
                git config user.name "Jenkins"
                git remote set-url origin https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/elevy99927/hello-newapp.git
                git add *.yaml *.yml
                git commit -m "Update YAML files - Build ${BUILD_NUMBER}"
                git push origin HEAD:${BRANCH_NAME}
            '''
        }
    }
}
```

This stage will:
- Configure git user settings
- Set the remote URL with authentication
- Add all YAML files to git
- Commit with build number
- Push to the current branch