pipeline {
    agent {label 'master'}
    parameters {
        booleanParam(name: 'WorldCities', defaultValue: true, description: 'Ingest World Cities Data to CH')
        booleanParam(name: 'Iris', defaultValue: false, description: 'Ingest Iris Data to CH')
    }
    stages {
		stage('Initialize'){
		    steps {
		        script {
		            def dockerHome = tool 'myDocker'
                    env.PATH = "${dockerHome}/bin:${env.PATH}"
                    env.SCRIPT = "/py_project/i_data/script.py"
		        }
		    }
        }

        stage('Ingest World Cities Data') {
            when { expression { params.WorldCities } }
            steps {
               sh "docker exec -it flask_app python ${env.SCRIPT} -t world_cities"
            }
        }

        stage('Ingest Iris Data') {
            when { expression { params.Iris } }
            steps {
               sh "docker exec -it flask_app python ${env.SCRIPT} -t iris"
            }
        }

    }
}