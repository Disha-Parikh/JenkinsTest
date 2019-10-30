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

	stage('docker build/push'){
		docker.withRegistry('https://index.docker.io/v1/','Docker'){
		def app = docker.build("dishaparikh98/finalflask:${commit_id}", '.').push()
}

	}
}
