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
                    . ./activeaza_venv_jenkins
                    '''
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                sh '''
                    cd app;
                    . ./activeaza_venv;
                    pytest;
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
