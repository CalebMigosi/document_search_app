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
                echo "Create test elastic search db"
                sh "./scripts/create_db.sh"

                echo 'Testing the application'
                sh "./scripts/run_tests.sh"
            }
        }

        stage("Deploy"){
            steps{
                echo 'Deploying the application'
            }
        }
    }

}