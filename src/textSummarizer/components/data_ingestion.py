""" 
Sure! Here's a summary of the provided Python code:

The code defines a `DataIngestion` class responsible for downloading and extracting data for the text summarization project. The class takes a `DataIngestionConfig` object as a parameter during initialization, which contains the necessary configuration for data ingestion.

The class has the following methods:

1. `download_file`: This method checks if the local data file specified in the configuration exists. If the file doesn't exist, it uses `urllib.request.urlretrieve` to download the file from the specified URL (`config.source_URL`) and save it to the local data file path (`config.local_data_file`). Information about the downloaded file, such as the filename and headers, is logged using the `logger` object. If the file already exists, the method logs the file's size without attempting to download it again.

2. `extract_zip_file`: This method extracts the contents of the zip file specified by `config.local_data_file` into the directory specified by `config.unzip_dir`. It creates the destination directory if it doesn't exist. The method uses the `zipfile` module to extract the contents of the zip file.

Overall, this code component handles the data ingestion process by downloading a file from a URL and extracting its contents from a zip file. It uses the provided configuration to determine the file paths and logging information.

"""

import os
import urllib.request as request
import zipfile
from textSummarizer.entity import DataIngestionConfig
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  

        
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            
    
""" 
import os: Imports the os module, which provides a way to interact with the operating system.

import urllib.request as request: Imports the urllib.request module and assigns it an alias request. This module allows for URL-related operations such as retrieving resources.

import zipfile: Imports the zipfile module, which provides functionality for working with ZIP archives.

from textSummarizer.logging import logger: Imports the logger object from the textSummarizer.logging module. It is assumed that the logger object is responsible for logging messages.

from textSummarizer.utils.common import get_size: Imports the get_size function from the textSummarizer.utils.common module. This function calculates the size of a file.

from pathlib import Path: Imports the Path class from the pathlib module, which provides an object-oriented approach to working with file paths.

from textSummarizer.entity import DataIngestionConfig: Imports the DataIngestionConfig class from the textSummarizer.entity module.

class DataIngestion:: Defines a class named DataIngestion for handling data ingestion operations.

def __init__(self, config: DataIngestionConfig):: Defines the initialization method for the DataIngestion class. It takes a config parameter of type DataIngestionConfig, which represents the configuration for data ingestion.

self.config = config: Assigns the config parameter to the config attribute of the DataIngestion instance.

def download_file(self):: Defines a method named download_file within the DataIngestion class for downloading a file.

if not os.path.exists(self.config.local_data_file):: Checks if the local data file specified in the configuration (config.local_data_file) does not exist using os.path.exists.

filename, headers = request.urlretrieve(url=self.config.source_URL, filename=self.config.local_data_file): Downloads the file from the specified URL (config.source_URL) and saves it to the local data file path (config.local_data_file) using urllib.request.urlretrieve. The downloaded file's name and headers are assigned to the filename and headers variables, respectively.

logger.info(f"{filename} download! with following info: \n{headers}"): Logs an informational message using the logger.info method, indicating that the file has been downloaded and includes the filename and headers information.

logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}"): Logs an informational message using the logger.info method, indicating that the file already exists and provides its size by calling the get_size function on the Path object representing the local data file.

def extract_zip_file(self):: Defines a method named extract_zip_file within the DataIngestion class for extracting a zip file.

unzip_path = self.config.unzip_dir: Assigns the unzip directory path specified in the configuration (config.unzip_dir) to the unzip_path variable.

os.makedirs(unzip_path, exist_ok=True): Creates the unzip directory specified by unzip_path using os.makedirs. The exist_ok=True argument ensures that the directory is created if it doesn't exist.

with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:: Opens the local data file specified in the configuration (config.local_data_file) as a zip file in read mode using zipfile.ZipFile. The with statement ensures that the zip file is automatically closed after the block.

zip_ref.extractall(unzip_path): Extracts all the contents of the zip file into the unzip directory specified by unzip_path using the extractall method of the zipfile.ZipFile object.

In summary, this code component defines a DataIngestion class that handles downloading files from a URL and extracting the contents of a zip file. It uses various modules and functions such as os, urllib.request, zipfile, logger, and pathlib to perform these operations based on the provided configuration.



"""