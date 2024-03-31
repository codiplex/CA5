pipeline {
    environment {
        DOCKERHUB_USERNAME = ''
        DATABASE_URL = 'postgresql://myuser:mypassword@database:5432/mydb'
    }

    agent any

    stages {
        stage('Login to Docker Hub') {
            steps {
                script {
                    // Use the Docker Hub credentials stored in Jenkins
                    withCredentials([usernamePassword(credentialsId: 'Docker-Codiplex', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_TOKEN')]) {
                        sh 'docker login -u $DOCKERHUB_USER -p $DOCKERHUB_TOKEN'
                        DOCKERHUB_USERNAME = DOCKERHUB_USER
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t postgresql-db-service:latest .'
            }
        }

        stage('Tag Docker Image') {
            steps {
                sh "docker tag postgresql-db-service:latest $DOCKERHUB_USERNAME/ca5-postgres:latest"
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                sh "docker push $DOCKERHUB_USERNAME/ca5-postgres:latest"
            }
        }

        stage('Check and Pull Docker Images') {
            steps {
                script {
                    // Define the image names
                    def frontendImageName = 'codiplex/ca4-app:latest'
                    def backendImageName = 'codiplex/ca4-postgres:latest'

                    // Check if the Docker images exist
                    def frontendImageExists = sh(script: "docker image ls -q ${frontendImageName}", returnStatus: true) == 0
                    def backendImageExists = sh(script: "docker image ls -q ${backendImageName}", returnStatus: true) == 0

                    // Pull the images if they don't exist
                    if (!frontendImageExists) {
                        sh "docker pull ${frontendImageName}"
                    }
                    if (!backendImageExists) {
                        sh "docker pull ${backendImageName}"
                    }
                }
            }
        }

        stage('Run Docker Containers') {
            steps {
                script {
                    // Run the Docker containers
                    sh "docker run -d -p 5432:5432 --name ca4-postgres codiplex/ca4-postgres:latest"
                    sh "docker run -d -p 8080:5000 -e DATABASE_URL=${DATABASE_URL} --name ca4-app --link ca4-postgres codiplex/ca4-app:latest"
                }
            }
        }
    }

    post {
        always {
            // Stop and remove the Docker containers
            sh "docker stop ca4-app ca4-postgres"
            sh "docker rm ca4-app ca4-postgres"
        }
    }
}
