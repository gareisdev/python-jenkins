pipeline {
    agent none

    stages {
        stage('Test') {

            agent {
                docker {
                    image 'python:3.11-buster' 
                }
           }

            steps {
                sh 'python3 -m venv venv'
                sh 'pip install -r requirements.txt'
                sh 'pytest tests/test.py'
            }
        }

        stage('Build') {
            agent {
                docker {
                    image 'python:3.11-buster' 
                }
            }
            steps {
                script {
                    // Define las variables necesarias
                    def dockerImageName = 'python-jenkins'
                    def dockerImageTag = '0.0.1'
                    def dockerFilePath = 'Dockerfile'
r
                    sh "docker build -t ${dockerImageName}:${dockerImageTag} -f ${dockerFilePath} ."
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    def dockerImageName = 'python_jenkins'
                    def dockerImageTag = '0.0.1'
                    def dockerHubRepository = 'lgareis/python-jenkins' // Cambia esto a tu repositorio en DockerHub

                    withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                        sh "docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD"
                    }

                    // Etiquetar la imagen
                    sh "docker tag ${dockerImageName}:${dockerImageTag} ${dockerHubRepository}:${dockerImageTag}"

                    // Subir la imagen a DockerHub
                    sh "docker push ${dockerHubRepository}:${dockerImageTag}"
                }
            }
        }
    }
}

