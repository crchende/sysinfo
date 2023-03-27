pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'cd app'
                sh '. ../.venv/bin/activate'
                //sh git clone -l --no-hardlines /home/cip/programare/git/sysinfo
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                sh pytest
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
