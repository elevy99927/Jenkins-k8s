pipelineJob('app-pipeline') {
  triggers {
    scm('* * * * *')
  }
  definition {
    cpsScm {
      scm {
        git {
          remote {
            url('https://github.com/elevy99927/Jenkins-k8s.git')
          }
          branch('main')
        }
      }
      scriptPath('Jenkinsfile')
    }
  }
}
