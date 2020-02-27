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
		        }
		    }
        }

        stage('Build Flask App Image') {
            when { expression { params.flask_app } }
            steps {
               sh "docker build -t flask_app:latest -f Docker/flask_app.df ."
               step([
                    $class: 'DockerComposeBuilder',
                    dockerComposeFile: 'Docker/docker-compose.yml',
                    option: [$class: 'StartService', scale: 1, service: 'flask_app'],
                    useCustomDockerComposeFile: true
               ])
            }
        }

        stage('Build Grafana Image') {
            when { expression { params.grafana } }
            steps {
               sh "docker build --build-arg GUAI=${params.GUAI} --build-arg GTMI=${params.GTMI} -t grafana:v6.6.2 -f Docker/grafana.df ."
               step([
                    $class: 'DockerComposeBuilder',
                    dockerComposeFile: 'Docker/docker-compose.yml',
                    option: [$class: 'StartService', scale: 1, service: 'grafana'],
                    useCustomDockerComposeFile: true
               ])
            }
        }

        stage('Spinup rSyslog') {
            when { expression { params.rsyslog } }
            steps {
               step([
                    $class: 'DockerComposeBuilder',
                    dockerComposeFile: 'Docker/docker-compose.yml',
                    option: [$class: 'StartService', scale: 1, service: 'rsyslog'],
                    useCustomDockerComposeFile: true
               ])
            }
        }

        stage('Build Clickhouse Image') {
            when { expression { params.clickhouse } }
            steps {
               echo "YTD"
            }
        }
    }
}