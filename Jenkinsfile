pipeline {
	agent any
	stages{
		//stage('SonarQube analysis') {
		//	steps {
		//		script {
		//			scannerHome = tool 'SonarQubeScanner'
		//		}
		//		withSonarQubeEnv('SonarQube') {
		//			sh '${scannerHome}/bin/sonar-scanner'
		//		}
		//	}
		//}
		stage('Build') {
			agent {
				docker {
					image 'python:2-alpine'
				}
			}
			steps {
				sh 'python -m py_compile app/hello.py'
			}
		}
		stage('Delivery') {
			agent {
				docker {
					image 'cdrx/pyinstaller-linux:python2'
				}
			}
			steps {
				sh 'pyinstaller --onefile app/hello.py'
			}
			post {
				success {
					archiveArtifacts 'dist/hello'
				}
			}
		}
	}
}
