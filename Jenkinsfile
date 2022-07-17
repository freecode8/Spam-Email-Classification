pipeline {
        agent any
            stages {
                stage('Clone Repository') {
                /* Cloning the repository to our workspace */
                steps {
                checkout scm
                }
             }
           stage('Build Image') {
                steps {
                sh ' docker build -t EmailClassificationapp:latest .'
                }
           }
           stage('Run Image') {
                steps {
                sh '  docker run -d -p 8501:8501 --name EmailClassification EmailClassificationapp:latest'
                }
           }
           stage('Testing'){
                steps {
                    echo 'Process Complete..'

                    }
           }
    }
}
