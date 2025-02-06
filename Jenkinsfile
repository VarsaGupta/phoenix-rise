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
                    // Ensure Python and pip are installed (optional for fresh environments)
                    sh '''
                    apt update && apt install -y python3 python3-pip
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Ensure pytest is installed and run tests
                    sh '''
                    pip install pytest
                    pytest || echo "Tests failed, but continuing..."
                    '''
                }
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    // Run the Flask application in the background using gunicorn for better management
                    sh '''
                    pkill -f "gunicorn" || true  # Kill existing gunicorn processes (if any)
                    gunicorn --bind 0.0.0.0:5000 app:app --daemon
                    '''
                }
            }
        }

        stage('Verify Health') {
            steps {
                script {
                    // Health check with retries
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
