# Creating the Jenkins CI/CD pipeline
pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv .venv'
                sh '.venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Train Model') {
            steps {
                sh '.venv/bin/python train.py'
            }
        }
        stage('Test Model') {
            steps {
                sh '.venv/bin/python test.py'
            }
        }
        stage('Deploy Model') {
            steps {
                sh 'docker build -t doml-iris-api .'
                sh 'docker rm -f doml-iris-api || true'
                sh 'docker run -d --name doml-iris-api -p 127.0.0.1:8000:8000 doml-iris-api'
            }
        }
    }
    post {
        success { echo 'Training, testing, and deployment completed' }
        failure { echo 'Pipeline failed — check Console Output' }
    }
}
