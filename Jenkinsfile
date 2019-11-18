pipeline {
	agent none
	options {
		skipStagesAfterUnstable()
	}
	stages{
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
		node {
			stage('SCM') {
				git 'https://github.com/kamilporwitaccenture/DevOpsDemo.git'
			}
			stage('SonarQube analysis') {
				def scannerHome = tool 'SonarScanner 4.0';
				withSonarQubeEnv('SonarQube') {
					sh "${scannerHome}/bin/sonar-scanner"
				}
			}
		}
	}
}
