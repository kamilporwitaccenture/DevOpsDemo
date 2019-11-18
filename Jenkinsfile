pipeline {
	agent none
	options {
		skipStagesAfterUnstable()
	}
	stages{
		stage('SCM') {
			steps {
				git url: 'https://github.com/kamilporwitaccenture/DevOpsDemo.git'
			}
		}		
		stage('Build and SonarQube analysis') {
			steps {
				def scannerHome = tool 'SonarScanner 4.0';
				withSonarQubeEnv('SonarQube') {
					sh "${scannerHome}/bin/sonar-scanner"
				}
			}
		}
	}
}
