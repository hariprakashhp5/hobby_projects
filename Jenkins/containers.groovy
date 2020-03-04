pipeline {
    agent {label 'master'}
    parameters {
        booleanParam(name: 'flask_app', defaultValue: true, description: 'Build Generic Python Backend application Image & spin a container')
        booleanParam(name: 'grafana', defaultValue: true, description: 'Build Grafana Image & spin a container')
        string(name: 'GUAI', defaultValue: '', description: 'Google Analytics UA ID')
        string(name: 'GTMI', defaultValue: '', description: 'Google Tag Manager ID')
        booleanParam(name: 'rsyslog', defaultValue: true, description: 'Create rSyslog Container')
        booleanParam(name: 'clickhouse', defaultValue: true, description: 'Build Clickhouse DB Image & spin a container')
    }
    stages {
		stage('Initialize'){
		    steps {
		        script {
		            def dockerHome = tool 'myDocker'
                    env.PATH = "${dockerHome}/bin:${env.PATH}"
                    env.COMPOSE_FILE = "Docker/docker-compose.yml"
		        }
		    }
        }

        stage('Build Flask App Image') {
            when { expression { params.flask_app } }
            steps {
               sh "KK=${params.KAGGLE_KEY} KU=${params.KAGGLE_USERNAME} docker-compose -f ${env.COMPOSE_FILE} up flask_app"
            }
        }

        stage('Build Grafana Image') {
            when { expression { params.grafana } }
            steps {
               sh "GUAI=${params.GUAI} GTMI=${params.GTMI} docker-compose -f ${env.COMPOSE_FILE} up grafana"
            }
        }

        stage('Spinup rSyslog') {
            when { expression { params.rsyslog } }
            steps {
               sh "docker-compose -f ${env.COMPOSE_FILE} up rsyslog"
            }
        }

        stage('Build Clickhouse Image') {
            when { expression { params.clickhouse } }
            steps {
               sh "docker-compose -f ${env.COMPOSE_FILE} up clickhouse"
            }
        }
    }
}