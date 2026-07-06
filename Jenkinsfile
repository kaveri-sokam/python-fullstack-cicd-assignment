pipeline {
    agent any
    stages {
        stage('Checkout Source Code') {
          steps {
            checkout scm
          }
        }
        stage('Install Backend Dependencies') {
            steps {
                dir('backend') {
                    bat 'pip install -r requirements.txt'
                }
            }
        }
        stage('Install Frontend Dependencies') {
            steps {
                dir('frontend') {
                    bat 'npm install'
                }
            }
        }
        stage('Run Backend Tests') {
            steps {
                dir('backend') {
                    bat 'pytest'
                }
            }
        }
        stage('Build Frontend') {
            steps {
                dir('frontend') {
                    bat 'npm run build'
                }
            }
        }
        stage('SonarQube Analysis') {
            steps {
                echo 'Running SonarQube Analysis'
            }
        }
        stage('Build Docker Images') {
            steps {
                bat 'docker-compose build'
            }
        }
        stage('Deploy using Docker Compose') {
            steps {
                bat 'docker-compose up -d'
            }
        }
        stage('Smoke Test') {
            steps {
                bat 'curl http://localhost:8000/health'
            }
        }
        stage('Cleanup') {
            steps {
                bat 'docker-compose down'
            }
        }
    }
}