pipeline {
    agent any

    environment {
        DATABASE_HOST = 'db'
        DATABASE_PORT = '5432'
        DATABASE_NAME = 'mydb'
        DATABASE_USER = 'postgres'
        DATABASE_PASSWORD = 'Postgres-123'
        DEBUG = 'false'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Brijesh-26/video_streamin_gito.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Migrations') {
            steps {
                script {
                    sh 'python manage.py migrate'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image using the Dockerfile
                    sh 'docker build -t ytprj .'
                }
            }
        }

        // stage('Run Tests') {
        //     steps {
        //         script {
        //             sh 'python manage.py test'
        //         }
        //     }
        // }

        stage('Deploy with Gunicorn') {
            steps {
                script {
                    sh 'docker-compose -f docker-compose.yml up -d'
                }
            }
        }

        stage('Clean up') {
            steps {
                script {
                    sh 'docker-compose down'
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
