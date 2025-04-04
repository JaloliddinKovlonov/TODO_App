    pipeline {
        agent any
        stages {
            stage('Clone') {
                steps {
                    git branch: 'main', url: 'https://github.com/JaloliddinKovlonov/TODO_App.git'
                }
            }
            stage('Build Docker container and run'){
                steps{
                    sh 'docker build -t todo-app .'
                    sh 'docker run -d --name todo-app -p 8000:8000 todo-app'
                }
            }
            stage('Wait for Docker container to start') {
                steps {
                    sh 'sleep 10'  // Adjust based on your app's startup time
                }
            }
            stage('Run Tests'){
                steps {
                    sh 'docker exec -it todo-app bash'
                    sh 'pytest'
                }
            }
            stage('Clean up Docker') {
                steps {
                    sh 'exit'
                    sh 'docker stop todo-app'
                    sh 'docker rm todo-app'
                }

            }   
        }
    }