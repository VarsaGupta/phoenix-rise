pipeline {
    agent any

    environment {
        FLASK_APP = 'app.py'
        FLASK_ENV = 'development'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'pytest'  // Assuming you have tests defined
                }
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    sh 'nohup python3 app.py &'
                }
            }
        }

        stage('Verify Health') {
            steps {
                script {
                    sh 'curl http://localhost:5000/health-monitor'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline finished successfully!'
        }

        failure {
            echo 'Pipeline failed.'
        }
    }
}
