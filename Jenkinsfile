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
      sudo pip3 install -r requirements.txt
      
    '''
    }
		 	 
	}



}

post{

    always{

      echo "ALWAYS"
 
    }


    success{
      echo "SUCCESS"
           echo "Post actions running"

       script{
      docker.withRegistry('https://index.docker.io/v1/','Docker'){
      app = docker.build("dishaparikh98/finalflask:${commit_id}", '.').push()
        }

        
        sh "docker-compose up -d"
        sh "docker-compose ps "
      }
    }

    failure{

      echo "FAILURE!"
    }

  }
}
