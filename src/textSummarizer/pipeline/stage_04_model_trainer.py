""" 
from textSummarizer.config.configuration import ConfigurationManager: Imports the ConfigurationManager class from the textSummarizer.config.configuration module. This class is responsible for managing the configuration settings.

from textSummarizer.conponents.model_trainer import ModelTrainer: Imports the ModelTrainer class from the textSummarizer.conponents.model_trainer module. This class handles the training process for the text summarization model.

from textSummarizer.logging import logger: Imports the logger object from the textSummarizer.logging module. This object is used for logging purposes.

class ModelTrainerTrainingPipeline:: Defines the ModelTrainerTrainingPipeline class.

def __init__(self):: Defines the initialization method for the ModelTrainerTrainingPipeline class. It doesn't have any specific implementation in this case.

def main(self):: Defines the main method within the ModelTrainerTrainingPipeline class. This method represents the main entry point of the training pipeline.

config = ConfigurationManager(): Creates an instance of the ConfigurationManager class, which manages the configuration settings.

model_trainer_config = config.get_model_trainer_config(): Retrieves the model trainer configuration using the get_model_trainer_config method from the ConfigurationManager class.

model_trainer_config = ModelTrainer(config=model_trainer_config): Creates an instance of the ModelTrainer class, passing the model trainer configuration as an argument.

model_trainer_config.train(): Calls the train method of the ModelTrainer instance, initiating the training process for the text summarization model.

Overall, this code sets up a training pipeline by instantiating the necessary components, retrieving the configuration, creating a ModelTrainer instance, and triggering the training process.

"""

from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_trainer import ModelTrainer
from textSummarizer.logging import logger


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()