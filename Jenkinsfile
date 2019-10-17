pipeline {
  agent any 
  stages {
    stage('build') {
      steps {
             sh '''
			pip3 install -r requirements.txt
			python3 /var/lib/jenkins/workspace/myproject_pipeline/app.py
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
	stage('Deploy'){
		steps{
		sh '''
			docker build -t finalflask .
			docker tag finalflask dishaparikh98/finalflask:2.0
			docker push dishaparikh98/finalflask:2.0
		'''
		}
	}
		
  }
}

