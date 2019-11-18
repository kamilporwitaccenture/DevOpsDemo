pipeline {
	agent none
	options {
		skipStagesAfterUnstable()
	}
	stages{
		stage('Build') {
			agent {
				docker {
					image 'flask-sample:latest'
				}
			}
			steps {
				sh 'python -m py_compile app/hello.py'
			}
		}
	}
}
