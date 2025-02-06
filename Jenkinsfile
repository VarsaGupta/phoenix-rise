pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                echo "Updating system and installing dependencies..."
                apt update && apt install -y python3 python3-pip
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running tests..."
                // Add your test commands here
            }
        }

        stage('Deploy Application') {
            steps {
                echo "Deploying application..."
                // Add your deployment commands here
            }
        }

        stage('Verify Health') {
            steps {
                echo "Verifying health..."
                // Add your health check commands here
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline finished!'
        }
    }
}
