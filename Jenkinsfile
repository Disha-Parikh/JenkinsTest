pipeline {
  agent any 
  stages {
    stage('build') {
      steps {
             sh '''
			pip3 install -r requirements.txt
			nohup python3 /var/lib/jenkins/workspace/myproject_pipeline/app.py &
		'''	 
            }
        }
	stage('test'){
		steps{
		sh '''
		sonar-scanner \
  		-Dsonar.projectKey=flaskjenkins \
  		-Dsonar.sources=. \
  		-Dsonar.host.url=http://69f6bd5c.ngrok.io:9000 \
  		-Dsonar.login=3c839b584f07a95344533b64e01d0b89dcbba188
		'''
			}
		}
	stage('Deploy'){
		steps{
		sh '''
			docker build -t finalflask .
			docker tag finalflask dishaparikh98/finalflask:3.0
			docker login -u dishaparikh98 -p 707c4e9b-5b7a-4725-b80d-5299d0446c19
			docker push dishaparikh98/finalflask:3.0
			docker run -dp 5002:5002 dishaparikh98/finalflask:3.0
					'''
		}
	}
	stage ("SonarQube analysis") {
     steps {
        script {
           STAGE_NAME = "SonarQube analysis"
		 // this is a PR build, run sonar analysis
              withSonarQubeEnv("Scan") {
                 sh "nohup /opt/sonarscanner/sonar-scanner-3.2.0.1227-linux/bin/sonar-scanner &"   
              }		
              }
           
        }
     }
  

  stage ("SonarQube Gate Keeper"){
  	steps{
  		script{
  			STAGE_NAME="SonarQube GateKeeper"
  			def qualitygate = waitForQualityGate()
  			if(qualitygate.status!="OK"){
  				error "Pipeline aborted ${qualitygate.status}"

  		}
  	}
  }
		
  }
  }
}


