""" 
This code defines three functions in the "util/common.py" module. Here's a summary of each function:

1. `read_yaml(path_to_yaml: Path) -> ConfigBox`: This function reads a YAML file specified by `path_to_yaml` and returns its content as a `ConfigBox` object. It first attempts to open the file and load its contents using `yaml.safe_load()`. If the file is empty, it raises a `ValueError`. If any other exception occurs, it re-raises the exception. It also logs a message indicating the successful loading of the YAML file.

2. `create_directories(path_to_directories: list, verbose=True)`: This function creates directories specified by the `path_to_directories` list. It iterates over each path in the list and uses `os.makedirs()` to create the directories. If a directory already exists, it does nothing (`exist_ok=True`). It can log a message indicating the creation of each directory if `verbose` is set to `True`.

3. `get_size(path: Path) -> str`: This function takes a file path (`Path` object) and returns the size of the file in kilobytes (KB) as a string. It uses `os.path.getsize()` to retrieve the file size in bytes, divides it by 1024 to convert it to KB, rounds it to the nearest integer, and returns the size as a string with the "KB" suffix.

These functions utilize various modules and dependencies, such as `os`, `yaml`, `box`, `pathlib`, and `textSummarizer.logging`. They also make use of the `ensure_annotations` decorator, which ensures type annotations are checked at runtime.
"""

import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns
    Args:
        path_to_yaml (str): path like input
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories
    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB
    Args:
        path (Path): path of the file
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

""" 

import os: This line imports the os module, which provides functions for interacting with the operating system.

from box.exceptions import BoxValueError: This line imports the BoxValueError exception from the box.exceptions module. This exception is raised when there is an issue with values stored in a Box object.

import yaml: This line imports the yaml module, which provides functions for working with YAML files.

from textSummarizer.logging import logger: This line imports the logger object from the textSummarizer.logging module. It is used for logging messages in the code.

from ensure import ensure_annotations: This line imports the ensure_annotations decorator from the ensure module. It is used to ensure that type annotations are checked at runtime.

from box import ConfigBox: This line imports the ConfigBox class from the box module. It is a configuration object that provides attribute-style access to dictionaries.

from pathlib import Path: This line imports the Path class from the pathlib module. It represents a path in the file system.

from typing import Any: This line imports the Any type from the typing module. It is used to indicate that a function can accept or return any type.

@ensure_annotations: This is a decorator that applies the ensure_annotations behavior to the following function. It ensures that type annotations are checked at runtime.

def read_yaml(path_to_yaml: Path) -> ConfigBox:: This line defines the read_yaml function that takes a Path object as the path_to_yaml argument and returns a ConfigBox object. It reads a YAML file and attempts to load its contents using yaml.safe_load(). It logs a message indicating the successful loading of the YAML file. If the file is empty, it raises a ValueError. If any other exception occurs, it re-raises the exception.

@ensure_annotations: This decorator applies the ensure_annotations behavior to the following function.

def create_directories(path_to_directories: list, verbose=True):: This line defines the create_directories function that takes a list of paths (path_to_directories) as an argument. It creates directories using os.makedirs() for each path in the list. If a directory already exists, it does nothing (exist_ok=True). If verbose is True, it logs a message indicating the creation of each directory.

@ensure_annotations: This decorator applies the ensure_annotations behavior to the following function.

def get_size(path: Path) -> str:: This line defines the get_size function that takes a Path object as the path argument and returns a string. It calculates the size of the file in kilobytes (KB) using os.path.getsize(), divides it by 1024, rounds it to the nearest integer, and returns the size as a string with the "KB" suffix.

These functions utilize various modules and dependencies, such as os, yaml, box, pathlib, and textSummarizer.logging. They make use of the imported objects and types to perform specific operations related to reading YAML files, creating directories, and retrieving file sizes.
"""