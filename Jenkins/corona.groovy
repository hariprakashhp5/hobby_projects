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

        stage('Update Corona DataSet') {
            steps {
               sh "docker exec -i flask_app python /py_project/i_data/script.py -t corona"
            }
        }

    }
}