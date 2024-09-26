import os
import logging
from pathlib import Path


logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

#define project name

name_of_project="chicken_disease_classification"

#create files
list_of_files=[".github/workflows/.gitkeep",
               f"src/{name_of_project}/__init__.py",
               f"src/{name_of_project}/components/__init__.py",
               f"src/{name_of_project}/utils/.__init__.py",
               f"src/{name_of_project}/config/__init__.py",
               f"src/{name_of_project}/config/configuration.py",
               f"src/{name_of_project}/pipeline/__init__.py",
               f"src/{name_of_project}/entity/__init__.py",
               f"src/{name_of_project}/constants/__init__.py",
               "config/config.yaml",
               "dvc.yaml",
               "params.yaml",
               "requirements.txt",
               "setup.py",
               "research/trials.ipynb",
               "test.py"]


for file_path in list_of_files:
    file_path=Path(file_path)
    filedir,filename=os.path.split(file_path)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Directory ; {filedir} for the filename {filename}")
    
    if (not os.path.exists(file_path))or(os.path.getsize(file_path)==0):
        with open(file_path,'w')as f:
            pass
            logging.info(f"Creating empty files : {file_path}")
    else:
        logging.info(f"{filename} already exists")