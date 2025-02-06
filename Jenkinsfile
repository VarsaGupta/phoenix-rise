pipeline {
    agent {
        docker {
            image 'python:3.11'
        }
    }
    
    stages {
        stage('Checkout') {
            steps {
                script {
                    echo "Checking out code..."
                    checkout scm
                }
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                script {
                    echo "Creating virtual environment..."
                    sh """
                        python -m venv ${VENV_DIR}
                        source ${VENV_DIR}/bin/activate
                    """
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo "Installing dependencies..."
                    sh """
                        source ${VENV_DIR}/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    """
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo "Running tests..."
                    sh """
                        source ${VENV_DIR}/bin/activate
                        pytest tests/ --junitxml=report.xml
                    """
                }
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    echo "Deploying application..."
                
                }
            }
        }

        stage('Verify Health') {
            steps {
                script {
                    echo "Verifying application health..."
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline execution completed."
        }
        success {
            echo "Pipeline executed successfully."
        }
        failure {
            echo "Pipeline failed."
        }
    }
}
