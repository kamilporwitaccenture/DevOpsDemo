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
	}
}
