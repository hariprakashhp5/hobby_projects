pipeline {
    agent {label 'master'}
	parameters {
        booleanParam(name: 'flask_app', defaultValue: true, description: 'Build Generic Python Backend application Image')
        booleanParam(name: 'grafana', defaultValue: true, description: 'Build Grafana Image')
        booleanParam(name: 'clickhouse', defaultValue: true, description: 'Build Clickhouse DB Image')
    }
    stages {
		stage('Setup') {
			steps {
			    def dockerHome = tool 'myDocker'
                env.PATH = "${dockerHome}/bin:${env.PATH}"
				script {
					echo "Dummy Setup"
				}
			}
		}
        stage('Build Flask App Image') {
			when { expression { params.flask_app } }
			agent {
				dockerfile {
					filename 'Docker/flask_app.df'
					dir '.'
					args '-t latest'
				}			
			}
            steps {
               echo 'Done!'
            }
        }
		stage('Build Grafana Image') {
			when { expression { params.grafana } }
			agent {
				dockerfile {
					filename 'Docker/grafana.df'
					dir '.'
					args '-t v6.6.2'
				}			
			}
            steps {
               echo 'Done'
            }
        }
    }
}