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
          sh "${sonarqubeScannerHome}/bin/sonar-scanner -e -Dsonar.host.url=http://localhost:9000 -Dsonar.login=${sonarLogin} -Dsonar.projectVersion=${env.BUILD_NUMBER} -Dsonar.projectKey=admin -Dsonar.sources=. "
        }
  
       withSonarQubeEnv('Scan') {
        }

        timeout(time: 10, unit: 'MINUTES'){
        qualitygate = waitForQualityGate()

        echo "ABCD ${qualitygate.status}"
        if(qualitygate.status != "OK") {
              error "Pipeline aborted due to quality gate coverage failure: ${qualitygate.status}"
                //waitForQualityGate abortPipeline: true
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

  stage('docker build/push'){
    steps{
      script{
      docker.withRegistry('https://index.docker.io/v1/','Docker'){
      app = docker.build("dishaparikh98/finalflask:${commit_id}", '.').push()
        }
      }  
 
    }
  }

}

post{

    always{
      echo "Post actions running"
    }


    success{
      echo "SUCCESS"
    }

    failure{

      echo "FAILURE :("
    }

  }
}
