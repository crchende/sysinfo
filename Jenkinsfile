pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                dir app
                sh '''
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
