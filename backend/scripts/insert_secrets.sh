#!/usr/bin/env bash
chmod +x -R ${env.WORKSPACE}
sudo apt-get update && sudo apt-get install -y curl
sudo apt-get install python3.10
curl -sSL https://install.python-poetry.org | python3
cd .. && cd .. cd backend
$HOME/.local/bin/poetry run python ./app/config/create_env_file.py