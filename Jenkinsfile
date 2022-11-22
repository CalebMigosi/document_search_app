pipeline{

    agent any

    stages {
        stage("Insert secrets"){
            steps{
                echo "Inserting environment secrets into .env file"
                echo "Running insert_secrets.sh"
                sh "./scripts/insert_secrets.sh"
            }
        }
        stage("Build containers"){
            steps{
                echo 'Building the application'
                sh "docker-compose up --build -d"
            }
        }

        stage("Run tests"){
            steps{
                echo 'Testing the application'
            }
        }

        stage("Deploy"){
            steps{
                echo 'Deploying the application'
            }
        }
    }

}