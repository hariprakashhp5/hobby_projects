pipeline {
    agent {label 'master'}
    stages {
		stage('Initialize'){
		    steps {
		        script {
		            def dockerHome = tool 'myDocker'
                    env.PATH = "${dockerHome}/bin:${env.PATH}"
		        }
		        echo "!!!!!!!!!!!!!!!!!!!!!"
		        echo env.PATH
		    }
        }

        stage('Build Flask App Image') {
            agent {
				dockerfile {
					filename 'Docker/flask_app.df'
					dir '.'
					args '-t flask_app:latest'
				}
			}
            steps {
               echo env.PATH
               sh "docker --version"
            }
        }

        stage('step 2') {
            steps {
               echo env.PATH
               sh "docker --version"
            }
        }
    }
}