#!/usr/bin/env bash
curl -sSL https://install.python-poetry.org | python3
source $HOME/.local/bin/poetry run python ../app/config/create_env_file.py