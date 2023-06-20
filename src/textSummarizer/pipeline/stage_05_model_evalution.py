""" 
This code defines a class named ModelEvaluationTrainingPipeline that performs model evaluation for a text summarization project. Here's a summary of the code:

The code imports necessary modules and classes such as ConfigurationManager, ModelEvaluation, and logger.
The ModelEvaluationTrainingPipeline class is defined, which has an empty __init__ method and a main method.
The main method performs the main steps of the model evaluation pipeline.
It creates an instance of ConfigurationManager to manage the project configuration.
It retrieves the model evaluation configuration from the ConfigurationManager.
It creates an instance of ModelEvaluation using the retrieved model evaluation configuration.
It calls the evaluate method of the ModelEvaluation instance to perform the model evaluation.
In summary, this code sets up and executes the model evaluation pipeline by retrieving the necessary configuration and utilizing the ModelEvaluation component.

"""
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_evaluation import ModelEvaluation
from textSummarizer.logging import logger



class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()


""" 

from textSummarizer.config.configuration import ConfigurationManager: Imports the ConfigurationManager class from the textSummarizer.config.configuration module.

from textSummarizer.conponents.model_evaluation import ModelEvaluation: Imports the ModelEvaluation class from the textSummarizer.conponents.model_evaluation module.

from textSummarizer.logging import logger: Imports the logger module from the textSummarizer.logging package.

class ModelEvaluationTrainingPipeline:: Defines a class named ModelEvaluationTrainingPipeline.

def __init__(self):: Defines the constructor method for the ModelEvaluationTrainingPipeline class.

def main(self):: Defines a method named main within the ModelEvaluationTrainingPipeline class.

config = ConfigurationManager(): Creates an instance of the ConfigurationManager class and assigns it to the config variable.

model_evaluation_config = config.get_model_evaluation_config(): Retrieves the model evaluation configuration using the get_model_evaluation_config() method of the ConfigurationManager instance and assigns it to the model_evaluation_config variable.

model_evaluation_config = ModelEvaluation(config=model_evaluation_config): Creates an instance of the ModelEvaluation class with the model_evaluation_config as the configuration parameter and assigns it back to the model_evaluation_config variable. This line seems to have a typo as the variable name and class name are the same.

model_evaluation_config.evaluate(): Calls the evaluate() method of the ModelEvaluation instance to perform the model evaluation.

In summary, this code sets up and executes the model evaluation pipeline by creating instances of ConfigurationManager and ModelEvaluation classes, retrieving the model evaluation configuration, and calling the evaluate() method to perform the evaluation.

"""