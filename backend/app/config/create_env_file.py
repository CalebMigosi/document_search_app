import os

DIR = os.path.dirname(__file__)
HOME_DIR = os.path.abspath(os.path.join(DIR, os.pardir, os.pardir, os.pardir))

with open(os.path.join(HOME_DIR, ".env"), "x") as f:
    for key, value in os.environ.items():
        f.write(f"{key}={value}")
