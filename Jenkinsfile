pipeline {
    agent any
    environment {
        // Will match the exact credentials we set up in Jenkins
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds') 
        IMAGE_NAME = "flask-app"
        DOCKERHUB_USER = "sohamdocker25" 
    }
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        stage('Unit Testing') {
            steps {
                sh '''
                rm -rf venv
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                pytest test_app.py
                '''
            }
        }
        stage('Containerize & Push') {
            steps {
                sh 'docker build -t ${DOCKERHUB_USER}/${IMAGE_NAME}:${BUILD_NUMBER} .'
                sh 'docker tag ${DOCKERHUB_USER}/${IMAGE_NAME}:${BUILD_NUMBER} ${DOCKERHUB_USER}/${IMAGE_NAME}:latest'
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'docker push ${DOCKERHUB_USER}/${IMAGE_NAME}:${BUILD_NUMBER}'
                sh 'docker push ${DOCKERHUB_USER}/${IMAGE_NAME}:latest'
            }
        }
        stage('Kubernetes Deployment') {
            steps {
                withKubeConfig([credentialsId: 'minikube-config']) {
                    sh 'kubectl apply -f deployment.yaml'
                    sh 'kubectl apply -f service.yaml'
                    sh 'kubectl rollout restart deployment/flask-app'
                }
            }
        }
    }
}
