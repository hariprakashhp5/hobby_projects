def CONTAINER_NAME="flask-app"
def CONTAINER_TAG="latest"
def HTTP_PORT="3039"
def HOST_PORT="3039"

node {

    stage('Initialize'){
        def dockerHome = tool 'myDocker'
        env.PATH = "${dockerHome}/bin:${env.PATH}"
    }

    stage('Checkout') {
        checkout scm
    }

    stage("Image Prune"){
        imagePrune(CONTAINER_NAME)
    }

    stage('Image Build'){
        imageBuild(CONTAINER_NAME, CONTAINER_TAG)
    }


    stage('Run App'){
        runApp(CONTAINER_NAME, CONTAINER_TAG, HTTP_PORT, HOST_PORT)
    }

}

def imagePrune(containerName){
    try {
        sh "docker image prune -f"
        sh "docker stop $containerName"
    } catch(error){}
}

def imageBuild(containerName, tag){
    //sh "docker build -t $containerName:$tag --no-cache ./Docker/"
    sh "docker build -t $containerName:$tag --no-cache -f Docker/Dockerfile ."
    echo "Image build complete"
}

def pushToImage(containerName, tag, dockerUser, dockerPassword){
    sh "docker login -u $dockerUser -p $dockerPassword"
    sh "docker tag $containerName:$tag $dockerUser/$containerName:$tag"
    sh "docker push $dockerUser/$containerName:$tag"
    echo "Image push complete"
}

def runApp(containerName, tag, httpPort, hostPort){
    sh "docker run -d --rm -p $hostPort:$httpPort --name $containerName $containerName:$tag"
    echo "Application started on port: ${hostPort} (http)"
}
