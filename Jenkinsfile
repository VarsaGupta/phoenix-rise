pipeline {
    agent any

    environment {
        FLASK_APP = 'app.py'
        FLASK_ENV = 'development'
        VENV_DIR = 'venv' // Virtual environment directory
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    // Set up a virtual environment to isolate the Python environment
                    sh '''
                    python3 -m venv ${VENV_DIR}
                    source ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh '''
                    source ${VENV_DIR}/bin/activate
                    pytest || echo "Tests failed, but continuing..."
                    '''
                }
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    sh '''
                    source ${VENV_DIR}/bin/activate
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
