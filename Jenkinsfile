def commit_id
def sonarqubeScannerHome 
def app
def qualitygate

pipeline{

  agent any

  stages{
	
	stage('SCM Checkout'){
    steps{
      
      checkout scm
      sh "git rev-parse --short HEAD > .git/commit-id"
      script{
      commit_id = readFile('.git/commit-id').trim()
    }
    }
    
	}
	stage('Build'){
    steps{

      sh '''
      pip3 install -r requirements.txt
      
    '''
    }
		 	 
	}
  stage('sonar-scanner') {
    steps{
      script{

          sonarqubeScannerHome = tool name: 'SonarQube', type: 'hudson.plugins.sonar.SonarRunnerInstallation'

        withCredentials([string(credentialsId: 'Sonarqube', variable: 'sonarLogin')]) 
        {
          sh "${sonarqubeScannerHome}/bin/sonar-scanner -e -Dsonar.host.url=http://localhost:9000 -Dsonar.login=${sonarLogin} -Dsonar.projectVersion=${env.BUILD_NUMBER} -Dsonar.projectKey=jenkins:flaskjenkins -Dsonar.sources=. "
        }
  
       withSonarQubeEnv('Scan') {
        }

        timeout(time: 5, unit: 'MINUTES'){
        qualitygate = waitForQualityGate()

        if(qualitygate.status != "OK") {
              error "Pipeline aborted due to quality gate coverage failure: ${qualitygate.status}"
                waitForQualityGate abortPipeline: true
        }
        else{ 
              sh "echo PASSED"
        }
      }
    }
  
  }
       
         /*timeout(time: 1, unit: 'MINUTES') {
        waitForQualityGate abortPipeline: true
        
  }*/}

 /* stage('docker build/push'){
    steps{
     

      sh "docker run -p 5002:5000 --net=host  dishaparikh98/finalflask:${commit_id}"  
      

 
    }
  }
*/
}

post{

    always{
      echo "Post actions running"

       script{
      docker.withRegistry('https://index.docker.io/v1/','Docker'){
      app = docker.build("dishaparikh98/finalflask:${commit_id}", '.').push()
        }

        
        sh "docker-compose up -d"
        sh "docker-compose ps "
      }
    }


    success{
      echo "SUCCESS"
    }

    failure{

      echo "FAILURE "
    }

  }
}
