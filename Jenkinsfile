node {
	stage('SonarQube analysis') {
		def scannerHome = tool 'SonarQubeScanner';
		withSonarQubeEnv('SonarQube') {
			sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=tescik"
		}
	}
}
