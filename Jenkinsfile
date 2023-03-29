pipeline {
    agent none

    stages {
        stage('Build') {
            agent any
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
        stage('Testare') {
            parallel {
                stages {
                    stage('Unit Testing cu pytest') {
                        agent any
                        steps {
                            echo 'Unit testing with Pytest...'
                            sh '''
                                cd app;
                                . ./activeaza_venv;
                                pytest;
                            '''
                        }
                    }
                    try {
                        stage('pylint - calitate cod') {
                            agent any
                            steps {
                                sh 'pylint'
                            }
                        }
                    } catch(e) {
                        echo "Codul nu este formatat si organizat corect, conform standardelor Python"
                        echo e.toString()
                    }
                }
            }
        }

        stage('Deploy') {
            agent any
            steps {
                echo 'IN lucru ! ...'
            }
        }
    }
}
