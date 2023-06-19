""" 
from textSummarizer.config.configuration import ConfigurationManager: Imports the ConfigurationManager class from the textSummarizer.config.configuration module. This class is responsible for managing the project's configuration.

from textSummarizer.conponents.data_validation import DataValiadtion: Imports the DataValiadtion class from the textSummarizer.conponents.data_validation module. This class is responsible for validating data files.

from textSummarizer.logging import logger: Imports the logger object from the textSummarizer.logging module, which is used for logging.

class DataValidationTrainingPipeline: Defines a class named DataValidationTrainingPipeline representing the data validation stage of the training pipeline.

def __init__(self):: Defines the initialization method for the DataValidationTrainingPipeline class. It doesn't take any parameters and doesn't perform any specific initialization steps.

def main(self):: Defines the main method within the DataValidationTrainingPipeline class. This method serves as the entry point for the data validation stage.

config = ConfigurationManager(): Creates an instance of the ConfigurationManager class to manage the project's configuration.

data_validation_config = config.get_data_validation_config(): Retrieves the data validation configuration by calling the get_data_validation_config method of the ConfigurationManager instance.

data_validation = DataValiadtion(config=data_validation_config): Creates an instance of the DataValiadtion class for data validation, passing the obtained data validation configuration as a parameter.

data_validation.validate_all_files_exist(): Invokes the validate_all_files_exist method of the DataValiadtion instance to perform the data validation process.

In summary, the code sets up a data validation pipeline by instantiating the necessary classes (ConfigurationManager and DataValiadtion) and invoking the data validation process through the main method of the DataValidationTrainingPipeline class.
"""

from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import DataValiadtion
from textSummarizer.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_files_exist()