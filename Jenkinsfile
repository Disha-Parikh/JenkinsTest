node{
	def commit_id
	stage('SCM Checkout'){
	 checkout scm
	 sh "git rev-parse --short HEAD > .git/commit-id"
	 commit_id = readFile('.git/commit-id').trim()
	}
	stage('Build'){
		 sh '''
			pip3 install -r requirements.txt
			
		'''	 
	}

        stage('sonar-scanner')
        {
       		 def sonarqubeScannerHome = tool name: 'SonarQube', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
	         withCredentials([string(credentialsId: 'Sonarqube', variable: 'sonarLogin')])
       		 {
	                	sh "/opt/sonarscanner/sonar-scanner-3.2.0.1227-linux/bin/sonar-scanner -e -Dsonar.host.url=http://localhost:9000 -Dsonar.login=${sonarLogin} -Dsonar.projectVersion=${env.BUILD_NUMBER} -Dsonar.projectKey=jenkins -D sonar.sources=. "
        }
    }


	stage('docker build/push'){
		docker.withRegistry('https://index.docker.io/v1/','Docker'){
		def app = docker.build("dishaparikh98/finalflask:${commit_id}", '.').push()
}

	}
}
