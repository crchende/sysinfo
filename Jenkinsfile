pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                dir app
                sh 'pwd'
                withPythonEnv(activeaza_venv_jenkins) {
                    sh 'pwd'
                }
                /*
                sh '''
                    cd app;
                    pwd;
                    ls -l;
                    . ./activeaza_venv_jenkins;
                    pytest
                    '''
                */
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
