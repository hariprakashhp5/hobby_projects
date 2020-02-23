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
					tag 'latest'
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
					tag 'v6.6.2'
				}			
			}
            steps {
               echo 'Done'
            }
        }
    }
}