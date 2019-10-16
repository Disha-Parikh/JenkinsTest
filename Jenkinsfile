pipeline {
  agent any 
  stages {
    stage('build') {
      steps {
             sh '''
		pip3 install -r requirements.txt
		nohup python3 /var/lib/jenkins/workspace/myproject_pipeline/Example/app.py &
		'''	 
            }
        }
	stage('test'){
		steps{
		sh '''
		sonar-scanner \
  		-Dsonar.projectKey=flaskjenkins \
  		-Dsonar.sources=. \
  		-Dsonar.host.url=http://localhost:9000 \
  		-Dsonar.login=3c839b584f07a95344533b64e01d0b89dcbba188
		'''
			}
		}
	stage("Quality Gate"){
		steps{
			timeout(time: 300, unit: 'SECONDS') {
              def qg = waitForQualityGate()
              if (qg.status != 'OK') {
                  error "Pipeline aborted due to quality gate failure: ${qg.status}"
              }
		}	
		}	
    }
   }
}
