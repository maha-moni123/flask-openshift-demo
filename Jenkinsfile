pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/maha-moni123/flask-openshift-demo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Add your test commands here (e.g. pytest)'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Add OpenShift or server deployment steps here'
            }
        }
    }
}
