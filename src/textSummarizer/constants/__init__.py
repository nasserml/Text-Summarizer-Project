""" 
from pathlib import Path: This line imports the Path class from the pathlib module. The Path class provides an object-oriented interface for working with file paths and directories.

CONFIG_FILE_PATH = Path("config/config.yaml"): This line creates a Path object named CONFIG_FILE_PATH and assigns it the file path "config/config.yaml". It represents the location of the configuration file for the machine learning project. The Path class allows convenient manipulation and access to various properties of the file path.

PARAMS_FILE_PATH = Path("params.yaml"): This line creates a Path object named PARAMS_FILE_PATH and assigns it the file path "params.yaml". It represents the location of the parameters file for the machine learning project. Similar to CONFIG_FILE_PATH, PARAMS_FILE_PATH provides a way to work with the file path using the Path class.

These constants, CONFIG_FILE_PATH and PARAMS_FILE_PATH, allow easy access to the respective file paths within the project. They can be used in other parts of the code to load or manipulate the configuration and parameter files.
"""
from pathlib import Path

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")