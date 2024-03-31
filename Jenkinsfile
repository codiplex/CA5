pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('Docker_Codiplex')
        IMAGE_NAME = 'codiplex/ca5-app'
        TAG = 'latest'
    }

    stages {
        

        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh "docker build -t ${IMAGE_NAME}:${TAG} ."

                    // Log in to Docker Hub using the credentials
                    withCredentials([usernamePassword(credentialsId: DOCKER_HUB_CREDENTIALS, usernameVariable: 'DOCKER_HUB_USERNAME', passwordVariable: 'DOCKER_HUB_PASSWORD')]) {
                        sh "docker login -u $DOCKER_HUB_USERNAME -p $DOCKER_HUB_PASSWORD"
                    }

                    // Push the Docker image to Docker Hub
                    sh "docker push ${IMAGE_NAME}:${TAG}"
                }
            }
        }
    }
}
