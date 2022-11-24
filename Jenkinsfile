pipeline{

    agent any

    stages {
        stage("Insert secrets"){
            steps{
                echo "Inserting environment secrets into .env file"
                echo "Running insert_secrets.sh"
                sh """chmod +x -R ${env.WORKSPACE} 
                     cd backend/scripts 
                     ./insert_secrets.sh           
                """
            }
        }
        stage("Build containers"){
            steps{
                echo 'Building the application'
                sh """chmod +x -R ${env.WORKSPACE}
                      sudo usermod -aG docker jenkins
                      sudo docker-compose up --build -d
                    """
            }
        }

        stage("Run tests"){
            steps{
                echo "Create test elastic search db"
                sh """cd backend/scripts && ./create_db.sh && ./run_tests.sh
                    """
            }
        }

        stage("Deploy"){
            steps{
                echo 'Deploying the application'
            }
        }
    }

}