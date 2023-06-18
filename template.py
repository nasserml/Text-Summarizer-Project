""" 
This code is a Python script that creates a project directory structure by creating directories and files based on a predefined list of file paths. It also logs the actions taken during the process.

Here is a summary of the code:

Import necessary modules: The script imports the os module, the Path class from the pathlib module, and the logging module.

Configure logging: The logging module is configured to log messages with a specific format and at the INFO level.

Define project information: The script defines a project_name variable, which represents the name of the project.

Define the list of files: The script creates a list_of_files variable, which is a list of file paths relative to the project directory. Each file path represents a file that should be created. Some paths include subdirectories.

Iterate over the list of files: The script iterates over each file path in the list_of_files.

Extract directory and filename: For each file path, the script extracts the directory path and the filename using the os.path.split() function.

Create directories if needed: If the extracted directory path is not empty, the script creates the directory using os.makedirs(), ensuring that the directory and its parent directories are created if they don't exist. The exist_ok=True parameter allows the function to skip creating the directory if it already exists.

Create empty files if needed: If the file doesn't exist or its size is 0 bytes, the script creates an empty file using open() with the 'w' mode. This step ensures that the file is present even if it's empty.

Log actions: The script logs each action taken during the process, including the creation of directories and empty files. The logging messages include information about the file or directory being created.

Check for existing files: If a file already exists and is not empty, the script logs a message indicating that the file already exists.

The purpose of this script is to automate the creation of the project directory structure and ensure that the necessary files and directories are in place.
"""

import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s:')

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)
    if filedir != "" :
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename} ")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} is already exists")
        


""" 
import os: Imports the os module, which provides a way to interact with the operating system.

from pathlib import Path: Imports the Path class from the pathlib module, which provides an object-oriented approach to working with file paths.

import logging: Imports the logging module, which is used for logging messages.

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:'): Configures the logging module to log messages at the INFO level and specifies the format of the log messages.

project_name = "textSummarizer": Defines a variable project_name with the value "textSummarizer", representing the name of the project.

list_of_files = [...]: Defines a list called list_of_files that contains the file paths to be created. The paths are specified as strings.

for filepath in list_of_files:: Begins a loop that iterates over each file path in the list_of_files list.

filepath = Path(filepath): Converts the file path string into a Path object, allowing for easier manipulation of the path components.

filedir, filename = os.path.split(filepath): Uses the os.path.split() function to split the file path into the directory path (filedir) and the filename (filename).

if filedir != "":: Checks if the filedir is not an empty string.

os.makedirs(filedir, exist_ok=True): Creates the directory specified by filedir using os.makedirs(). The exist_ok=True parameter ensures that the directory is created only if it doesn't already exist.

logging.info(f"Creating directory:{filedir} for the file {filename}"): Logs an information message indicating the creation of the directory and the associated filename.

if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):: Checks if the file specified by filepath does not exist or if its size is 0 bytes.

with open(filepath,'w') as f: ...: Opens the file specified by filepath in write mode and assigns the file object to the variable f. The with statement ensures that the file is automatically closed after the block is executed.

pass: Placeholder statement that does nothing. This line is used to create an empty file.

logging.info(f"Creating empty file: {filepath}"): Logs an information message indicating the creation of the empty file.

logging.info(f"{filename} is already exists"): Logs an information message indicating that the file specified by filename already exists.

The purpose of this code is to create directories and files based on the specified file paths in the list_of_files list. It also logs the actions taken during the process, such as creating directories and empty files.
"""