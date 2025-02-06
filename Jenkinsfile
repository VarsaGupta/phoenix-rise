pipeline {
    agent any

    environment {
        PYTHON = "/usr/bin/python3"
        PIP = "/usr/bin/pip3"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Cloning repository..."
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Updating system and installing dependencies..."
                sh '''
                sudo apt update
                sudo apt install -y python3 python3-pip
                pip3 install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running unit tests..."
                sh '''
                pip3 install pytest
                pytest --maxfail=1 --disable-warnings
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                echo "Deploying Flask application..."
                sh 'nohup python3 app.py &'
            }
        }

        stage('Verify Health') {
            steps {
                echo "Checking if the application is running..."
                sh 'curl -f http://localhost:5000/health-monitor || exit 1'
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}
