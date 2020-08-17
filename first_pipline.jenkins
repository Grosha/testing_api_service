pipeline {
    agent { docker { image 'python:3.7' } }
    stages {
        stage('docker build') {
            steps {
                sh 'python --version'
            }
        }
        stage('get hostname') {
            steps {
                sh 'ssh groskka@192.168.1.12 \'hostname\''
            }
        }
    }
}