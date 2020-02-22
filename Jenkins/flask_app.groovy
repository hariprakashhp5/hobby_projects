def HTTP_PORT="3039"

node {

    stage('Initialize'){
        def dockerHome = tool 'myDocker'
        env.PATH = "${dockerHome}/bin:${env.PATH}"
    }

    stage('Checkout') {
        checkout scm
    }

    stage("Image Prune"){
        imagePrune(env.CONTAINER_NAME)
    }

    stage('Image Build'){
        imageBuild(env.CONTAINER_NAME, env.CONTAINER_TAG)
    }


    stage('Run App'){
        runApp(env.CONTAINER_NAME, env.CONTAINER_TAG, HTTP_PORT, env.HOST_PORT)
    }

}

def imagePrune(containerName){
    try {
        sh "docker image prune -f"
        sh "docker stop $containerName"
    } catch(error){}
}

def imageBuild(containerName, tag){
    sh "docker build -t $containerName:$tag -f Docker/$containerName_dockerfile ."
    echo "Image build complete"
}

def runApp(containerName, tag, httpPort, hostPort){
    sh "docker run -d --rm -p $hostPort:$httpPort --name $containerName $containerName:$tag"
    echo "Application started on port: ${hostPort} (http)"
}
