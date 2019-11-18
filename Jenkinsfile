pipeline {
	agent none
	options {
		skipStageAfterUnstable()
	}
	stages{
		stage('Build') {
			agent {
				docker {
					image 'flask-sample:latest'
				}
			}
			steps {
				sh 'python hello.py'
			}
		}
	}
}
