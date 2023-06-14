def branch = env.BRANCH_NAME
def build = env.BUILD_NUMBER
def DEBUG = true
def appname ="helloworld"
def DEPLOY = false
def artifactory = "docker.io" 
def repo = "elevy99927" # ***Put your  repo here!! ***
def appimage = "${artifactory}/${repo}/${appname}"
def apptag = "${build}"

def kubernetesurl = "https://kubernetes.default.svc"

if (branch == "dev"){
echo "----------  dev   -------"
kubernetesurl = "https://kubernetes.default.svc"
} else if  (branch == "qa"){
echo "----------  qa   -------"
} else if  (branch == "main"){
echo "----------  master   -------"
} else {

}


podTemplate(containers: [
      containerTemplate(name: 'jnlp', image: 'jenkins/inbound-agent', ttyEnabled: true),
      containerTemplate(name: 'docker', image: 'busybox:latest', ttyEnabled: true)
  ],
  volumes: [
     
  ]) {
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
}

