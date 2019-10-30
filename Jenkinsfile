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
}