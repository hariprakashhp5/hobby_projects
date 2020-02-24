pipeline {
    agent {label 'master'}
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
            steps {
               sh "docker build -t grafana:v6.6.2 -f Docker/grafana.df ."
            }
        }
    }
}