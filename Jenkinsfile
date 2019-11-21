pipeline {
	agent any
	stages{
		stage('SonarQube analysis') {
			environment {
				scannerHome = tool 'SonarQubeScanner'
			}
			steps {
				withSonarQubeEnv('SonarQube') {
					sh '${scannerHome}/bin/sonar-scanner'
				}

				timeout(time: 10, unit: 'MINUTES') {
					waitForQualityGate abortPipeline: true
				}
			}
		}
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
		stage('Deploy') {
			steps {
				sh 'docker build -t flask-sample:latest .'
				sh 'docker-compose up --detach --build'
			}
		}
	}
}
