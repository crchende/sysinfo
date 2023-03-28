pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh '''
                    pwd;
                    ls -l;
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
