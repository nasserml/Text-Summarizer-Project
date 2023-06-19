""" 

import os: Importing the os module for operating system related functionalities.

from textSummarizer.logging import logger: Importing the logger object from the textSummarizer.logging module.

from textSummarizer.entity import DataValidationConfig: Importing the DataValidationConfig class from the textSummarizer.entity module.

class DataValidation: Defining the DataValidation class responsible for validating the existence of required files.

The __init__ method within DataValidation initializes the class instance with a DataValidationConfig object.

The validate_all_files_exist method within DataValidation validates the existence of all required files. It retrieves the list of files in the specified directory, and for each file, it checks if it exists in the list of required files. If a file is missing, it sets the validation_status to False and writes the validation status to a file specified in the DataValidationConfig object. If all required files are present, it sets the validation_status to True and writes the validation status to the file. Finally, it returns the validation_status.

The try block starts, where the code attempts to validate the existence of files. If an exception occurs during the validation process, it is caught in the except block, and the exception is raised again.

Overall, the code snippet defines a DataValidation class that takes a configuration object and provides a method to validate the existence of required files in a specified directory.
"""

import os
from textSummarizer.entity import DataValidationConfig
from textSummarizer.logging import logger

class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    
    def validate_all_files_exist(self)-> bool:
        try:
            validation_status = None

            all_files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))

            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e


""" 
import os: Imports the os module, which provides functions for interacting with the operating system.

from textSummarizer.logging import logger: Imports the logger object from the textSummarizer.logging module, which is used for logging.

from textSummarizer.entity import DataValidationConfig: Imports the DataValidationConfig class from the textSummarizer.entity module, which represents the configuration for data validation.

class DataValidation: Defines a class named DataValidation responsible for data validation.

def __init__(self, config: DataValidationConfig): Defines the initialization method for the DataValidation class. It takes a DataValidationConfig object as a parameter and assigns it to the config attribute of the instance.

def validate_all_files_exist(self) -> bool: Defines a method named validate_all_files_exist within the DataValidation class. It returns a boolean value indicating the validation status of all files.

try:: Starts a try block to handle potential exceptions that may occur during the execution of the code.

validation_status = None: Initializes the validation_status variable to None.

all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset")): Retrieves the list of files in the specified directory ("artifacts/data_ingestion/samsum_dataset") using the os.listdir() function and assigns it to the all_files variable.

for file in all_files:: Iterates over each file in the all_files list.

if file not in self.config.ALL_REQUIRED_FILES:: Checks if the current file is not present in the list of all required files specified in the DataValidationConfig object.

validation_status = False: Sets the validation_status to False since a required file is missing.

with open(self.config.STATUS_FILE, 'w') as f:: Opens the file specified in the STATUS_FILE attribute of the DataValidationConfig object in write mode.

f.write(f"Validation status: {validation_status}"): Writes the validation status (False) to the file.

else:: If the file is present in the list of required files.

validation_status = True: Sets the validation_status to True since all required files are present.

with open(self.config.STATUS_FILE, 'w') as f:: Opens the file specified in the STATUS_FILE attribute of the DataValidationConfig object in write mode.

f.write(f"Validation status: {validation_status}"): Writes the validation status (True) to the file.

return validation_status: Returns the final validation status after checking all files.

except Exception as e:: Catches any exception that occurs within the try block and assigns it to the variable e.

raise e: Raises the exception again to propagate it to the caller.

The code defines a DataValidation class that takes a DataValidationConfig object as input and provides a method to validate the existence of required files in a specific directory.

"""