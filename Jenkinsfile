pipeline {
    environment {
        DOCKERHUB_USERNAME = ''
    }

    agent any

    stages {
        stage('Login to Docker Hub') {
            steps {
                script {
                    // Use the Docker Hub credentials stored in Jenkins
                    withCredentials([usernamePassword(credentialsId: 'misfits-dockerhub-credentials', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_TOKEN')]) {
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
    }
}
