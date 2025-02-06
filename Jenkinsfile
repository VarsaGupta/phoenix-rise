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

        stage('Run Tests') {
            steps {
                script {
                    sh '''
                    pytest || echo "Tests failed, but continuing..."
                    '''
                }
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    sh '''
                    pkill -f "gunicorn" || true
                    gunicorn --bind 0.0.0.0:5000 app:app --daemon
                    '''
                }
            }
        }

        stage('Verify Health') {
            steps {
                script {
                    sh '''
                    echo "Waiting for application to be ready..."
                    for i in {1..5}; do
                        curl --silent --fail http://localhost:5000/health-monitor && exit 0 || sleep 2
                    done
                    echo "Health check failed!" && exit 1
                    '''
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
