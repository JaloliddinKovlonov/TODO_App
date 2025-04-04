pipeline {
    agent {
        docker { image 'python:3.9' }
    }
    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/JaloliddinKovlonov/TODO_App.git'
            }
        }
        stage('Install Dependencies'){
            steps{
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests'){
            steps {
                sh 'pytest'
            }
        }
    }
}