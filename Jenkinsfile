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
        stage('Run Tests'){
            steps {
                sh 'pytest'
            }
        }
    }
}