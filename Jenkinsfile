pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh '''
                    cd app;
                    pwd;
                    ls -l;
                    . ./activeaza_venv;
                    pytest
                    '''
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
