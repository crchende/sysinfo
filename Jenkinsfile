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
                    . ./activeaza_venv
                    '''
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                sh '''
                    . ./activeaza_venv
                    pytest
                '''
                //sh pytest
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
