pipeline{

    agent any

    stages {
        stage("Insert secrets"){
            steps{
                echo "Inserting environment secrets into .env file"
                echo "Running insert_secrets.sh"
                sh """
                    chmod +x -R ${env.WORKSPACE}
                    sudo apt-get update && sudo apt-get install -y curl
                    sudo apt-get install python3.10
                    curl -sSL https://install.python-poetry.org | python3
                    cd backend
                    $HOME/.local/bin/poetry run python ./app/config/create_env_file.py            
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
                sh "chmod +x -R ${env.WORKSPACE}"
                sh "./scripts/create_db.sh"

                echo 'Testing the application'
                sh "./backend/scripts/run_tests.sh"
            }
        }

        stage("Deploy"){
            steps{
                echo 'Deploying the application'
            }
        }
    }

}