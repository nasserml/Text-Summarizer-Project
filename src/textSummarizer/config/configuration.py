""" 
This code defines a ConfigurationManager class responsible for managing the configuration of the text summarization project. Here's the summary of the code:

from textSummarizer.constants import *: This line imports all the constants defined in the constants module of the textSummarizer package. These constants are used as global variables in the configuration.

from textSummarizer.utils.common import read_yaml, create_directories: This line imports the read_yaml and create_directories functions from the common module of the textSummarizer.utils package. These functions are utility functions for reading YAML files and creating directories, respectively.

from textSummarizer.entity import (...): This line imports the data classes from the entity module of the textSummarizer package. These data classes represent different configurations for data ingestion, data validation, data transformation, model training, and model evaluation.

class ConfigurationManager:: This line defines the ConfigurationManager class, which is responsible for managing the project's configuration.

def __init__(self, config_filepath = CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH):: This line defines the constructor of the ConfigurationManager class. It takes optional arguments for the configuration file path and the parameters file path. By default, it uses the global constants CONFIG_FILE_PATH and PARAMS_FILE_PATH.

self.config = read_yaml(config_filepath): This line reads the configuration YAML file specified by config_filepath and assigns the resulting configuration to the self.config attribute.

self.params = read_yaml(params_filepath): This line reads the parameters YAML file specified by params_filepath and assigns the resulting parameters to the self.params attribute.

create_directories([self.config.artifacts_root]): This line creates the necessary directories specified by the artifacts_root attribute in the configuration. The create_directories function is called with a list containing the root directory path.

The ConfigurationManager class also includes several methods for retrieving specific configurations:

get_data_ingestion_config: Retrieves the data ingestion configuration by extracting the relevant attributes from self.config.data_ingestion and creating an instance of the DataIngestionConfig class.
get_data_validation_config: Retrieves the data validation configuration by extracting the relevant attributes from self.config.data_validation and creating an instance of the DataValidationConfig class.
get_data_transformation_config: Retrieves the data transformation configuration by extracting the relevant attributes from self.config.data_transformation and creating an instance of the DataTransformationConfig class.
get_model_trainer_config: Retrieves the model trainer configuration by extracting the relevant attributes from self.config.model_trainer and self.params.TrainingArguments and creating an instance of the ModelTrainerConfig class.
get_model_evaluation_config: Retrieves the model evaluation configuration by extracting the relevant attributes from self.config.model_evaluation and creating an instance of the ModelEvaluationConfig class.
In each of these methods, the create_directories function is called to create the required directories specified in the configuration.

Overall, this code provides a convenient way to manage and access different configurations in the text summarization project.

"""

from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.entity import (DataIngestionConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config


""" 
he code you provided defines a ConfigurationManager class, which is responsible for managing the configuration of a text summarization project. Here's an explanation of each line:

from textSummarizer.constants import *: This line imports all the constants defined in the constants module of the textSummarizer package. The * allows importing all the constants at once.

from textSummarizer.utils.common import read_yaml, create_directories: This line imports the read_yaml and create_directories functions from the common module of the textSummarizer.utils package. These functions are utility functions used for reading YAML files and creating directories, respectively.

from textSummarizer.entity import (...): This line imports several classes from the entity module of the textSummarizer package. These classes represent different configurations related to data ingestion, data validation, data transformation, model training, and model evaluation.

class ConfigurationManager:: This line starts the definition of the ConfigurationManager class, which manages the project's configuration.

def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):: This line defines the constructor of the ConfigurationManager class. It takes two optional arguments, config_filepath and params_filepath, with default values provided by the constants CONFIG_FILE_PATH and PARAMS_FILE_PATH.

self.config = read_yaml(config_filepath): This line reads the configuration file specified by config_filepath using the read_yaml function and assigns the result to the self.config attribute.

self.params = read_yaml(params_filepath): This line reads the parameters file specified by params_filepath using the read_yaml function and assigns the result to the self.params attribute.

create_directories([self.config.artifacts_root]): This line creates the necessary directories specified by the artifacts_root attribute in the configuration. The create_directories function is called with a list containing the root directory path.

The ConfigurationManager class also includes several methods for retrieving specific configurations:

get_data_ingestion_config: This method retrieves the data ingestion configuration from the self.config attribute. It creates an instance of the DataIngestionConfig class with the relevant attributes extracted from the configuration and returns it.

get_data_validation_config: This method retrieves the data validation configuration from the self.config attribute. It creates an instance of the DataValidationConfig class with the relevant attributes extracted from the configuration and returns it.

get_data_transformation_config: This method retrieves the data transformation configuration from the self.config attribute. It creates an instance of the DataTransformationConfig class with the relevant attributes extracted from the configuration and returns it.

get_model_trainer_config: This method retrieves the model trainer configuration from the self.config and self.params attributes. It creates an instance of the ModelTrainerConfig class with the relevant attributes extracted from the configuration and parameters, and returns it.

get_model_evaluation_config: This method retrieves the model evaluation configuration from the self.config attribute. It creates an instance of the ModelEvaluationConfig class with the relevant attributes extracted from the configuration and returns it.

Each method also includes a line to create the necessary directories specified by the root_dir attribute in the respective configuration.

In summary, the ConfigurationManager class provides a way to manage and access various configurations required for the text summarization project. It loads the configuration and parameter files, creates directories, and provides methods to retrieve specific configurations as needed. The class follows a modular approach by utilizing separate data classes (DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, and ModelEvaluationConfig) to encapsulate and organize the configuration parameters specific to each aspect of the project.

The ConfigurationManager class ensures that the necessary directories are created and provides convenient methods to access each configuration. By separating the configuration logic into a dedicated class, it promotes code readability, reusability, and maintainability.

Overall, the code demonstrates good software engineering practices by modularizing the configuration management and promoting code organization and encapsulation.

The self.config = read_yaml(config_filepath) line reads the YAML configuration file specified by config_filepath using the read_yaml function from the textSummarizer.utils.common module. The parsed configuration is stored in the self.config attribute.

The self.params = read_yaml(params_filepath) line reads another YAML file specified by params_filepath and stores the parsed parameters in the self.params attribute.

The create_directories([self.config.artifacts_root]) line creates the necessary directories specified by the artifacts_root attribute in the configuration.

The get_data_ingestion_config method returns an instance of the DataIngestionConfig class, populated with the relevant configuration parameters for data ingestion.

The get_data_validation_config method returns an instance of the DataValidationConfig class, containing the configuration parameters for data validation.

The get_data_transformation_config method returns an instance of the DataTransformationConfig class, which encapsulates the configuration parameters for data transformation.

The get_model_trainer_config method returns an instance of the ModelTrainerConfig class, populated with the configuration parameters for model training. It also includes parameters from the params attribute.

The get_model_evaluation_config method returns an instance of the ModelEvaluationConfig class, containing the configuration parameters for model evaluation.

These methods provide convenient access to the specific configurations needed for different parts of the machine learning project, allowing for easy retrieval and management of the configuration data.

Overall, this code demonstrates a well-organized approach to configuration management in a machine learning project, separating different aspects of the project into individual configuration classes and providing a central ConfigurationManager class for accessing and managing these configurations.

he from textSummarizer.constants import * line imports all the constants defined in the textSummarizer.constants module.

The from textSummarizer.utils.common import read_yaml, create_directories line imports the read_yaml and create_directories functions from the textSummarizer.utils.common module.

The from textSummarizer.entity import (DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig) line imports the data entity classes DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, and ModelEvaluationConfig from the textSummarizer.entity module.

The ConfigurationManager class is defined, which serves as a central configuration manager for the text summarization project.

The __init__ method initializes an instance of ConfigurationManager. It takes two optional arguments config_filepath and params_filepath, which default to the values of CONFIG_FILE_PATH and PARAMS_FILE_PATH respectively.

Inside the __init__ method, the configuration file and parameters file are read using the read_yaml function. The parsed configuration is stored in the self.config attribute, and the parsed parameters are stored in the self.params attribute.

The create_directories([self.config.artifacts_root]) line creates the necessary directories specified by the artifacts_root attribute in the configuration.

The get_data_ingestion_config method returns an instance of the DataIngestionConfig class, which is initialized with the relevant configuration parameters for data ingestion.

The get_data_validation_config method returns an instance of the DataValidationConfig class, which contains the configuration parameters for data validation.

The get_data_transformation_config method returns an instance of the DataTransformationConfig class, which encapsulates the configuration parameters for data transformation.

The get_model_trainer_config method returns an instance of the ModelTrainerConfig class, which is populated with the configuration parameters for model training. It also includes parameters from the params attribute.

The get_model_evaluation_config method returns an instance of the ModelEvaluationConfig class, which contains the configuration parameters for model evaluation.

These methods provide a convenient way to access different configurations required for various parts of the text summarization project. The ConfigurationManager class centralizes the management of these configurations, making it easier to retrieve and use the configuration data throughout the project.

The create_directories([config.root_dir]) line inside each configuration method creates the necessary directories specified by the root_dir attribute of the corresponding configuration class.

The data_ingestion_config, data_validation_config, data_transformation_config, model_trainer_config, and model_evaluation_config objects are initialized with the respective configuration parameters obtained from the self.config attribute. These objects represent the configurations for data ingestion, data validation, data transformation, model training, and model evaluation, respectively.

Each configuration object is returned at the end of its respective method, providing a convenient way to access the configuration parameters specific to each component of the text summarization project.

The ConfigurationManager class acts as a central component for managing and retrieving various configurations used throughout the project. By organizing the configurations into separate classes and providing dedicated methods to access them, it promotes modular and maintainable code. Additionally, the use of dataclass decorators allows for convenient initialization and immutability of the configuration objects.
"""