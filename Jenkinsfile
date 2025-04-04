pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/JaloliddinKovlonov/TODO_App.git'
            }
        }
        stage('Install Dependencies'){
            steps{
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Run Tests'){
            steps {
                sh '. venv/bin/activate && PYTHONPATH=. pytest'
            }
        }
    }
}