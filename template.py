import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s :')

package_name="deepClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",  ## .gitkeep is a kind of placeholder file as empty folder are not uploaded on github. This is used to create structure
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/componenets/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini", # local testing file
    "research/trails.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory : {filedir} for file: {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating Empty file : {filedir}")
    else:
        logging.info(f"File already created : {filepath}")