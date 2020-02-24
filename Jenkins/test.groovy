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
            steps {
               echo env.PATH
               echo 'Done!'
            }
        }
    }
}