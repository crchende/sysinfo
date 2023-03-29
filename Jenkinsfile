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

                stage('pylint - calitate cod') {
                    agent any
                    steps {
                        sh '''
                            cd app;
                            . ./activeaza_venv;
                            echo '\n\nVerificare lib/*.py cu pylint\n';
                            pylint lib/*.py;

                            echo '\n\nVerificare tests/*.py cu pylint';
                            pylint;

                            echo '\n\nVerificare sysinfo.py cu pylint';
                            pylint sysinfo.py;
                        '''
                    }
                }
                /*catch(e) {
                        echo "Codul nu este formatat si organizat corect, conform standardelor Python"
                        echo e.toString()
                    }*/
                //{}
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
