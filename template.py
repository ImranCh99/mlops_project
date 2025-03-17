import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "mlops_project"

list_of_files = [
    ".github/workflows/.gitkeep", # directory for CICD Github actions
    "src/cnnClassifier/__init_.py",
    "src/cnnClassifier/components/__init_.py",
    "src/cnnClassifier/utils/__init_.py",
    "src/cnnClassifier/config/__init_.py",
    "src/cnnClassifier/pipeline/__init_.py",
    "src/cnnClassifier/entity/__init_.py",
    "src/cnnClassifier/constants/__init_.py",
    "config/config.yaml",   # configuration file
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass  # creating an empty file
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} is already exists")