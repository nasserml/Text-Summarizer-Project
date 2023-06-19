""" 
This Python code defines several data classes in the file Text-Summarization-NLP-Project/src/textSummarizer/entity/__init__.py for different aspects of a machine learning project related to text summarization. Here's a summary of each class:

DataIngestionConfig: This data class represents the configuration for data ingestion. It has the following attributes:

root_dir (Path): The root directory path for data ingestion.
source_URL (str): The source URL for the data.
local_data_file (Path): The local data file path.
unzip_dir (Path): The directory path for unzipping the data.
DataValidationConfig: This data class represents the configuration for data validation. It has the following attributes:

root_dir (Path): The root directory path for data validation.
STATUS_FILE (str): The file path for the status file.
ALL_REQUIRED_FILES (list): A list of required files.
DataTransformationConfig: This data class represents the configuration for data transformation. It has the following attributes:

root_dir (Path): The root directory path for data transformation.
data_path (Path): The path to the data.
tokenizer_name (Path): The path to the tokenizer.
ModelTrainerConfig: This data class represents the configuration for model training. It has several attributes including:

root_dir (Path): The root directory path for model training.
data_path (Path): The path to the training data.
model_ckpt (Path): The path to the model checkpoint.
num_train_epochs (int): The number of training epochs.
warmup_steps (int): The number of warm-up steps.
per_device_train_batch_size (int): The batch size for training.
weight_decay (float): The weight decay value.
logging_steps (int): The steps interval for logging.
evaluation_strategy (str): The strategy for evaluation.
eval_steps (int): The steps interval for evaluation.
save_steps (float): The steps interval for saving the model.
gradient_accumulation_steps (int): The steps interval for gradient accumulation.
ModelEvaluationConfig: This data class represents the configuration for model evaluation. It has the following attributes:

root_dir (Path): The root directory path for model evaluation.
data_path (Path): The path to the evaluation data.
model_path (Path): The path to the trained model.
tokenizer_path (Path): The path to the tokenizer.
metric_file_name (str): The file name for storing evaluation metrics.
These data classes provide a structured way to store and access configuration settings for various components of the text summarization machine learning project.
"""

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list
    

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path



""" 
from dataclasses import dataclass: This line imports the dataclass decorator from the dataclasses module. The dataclass decorator simplifies the process of creating classes that primarily hold data.

from pathlib import Path: This line imports the Path class from the pathlib module. The Path class provides an object-oriented interface for working with file paths and directories.

@dataclass(frozen=True): This line is a decorator that indicates that the following class is a data class. The frozen=True argument makes instances of the class immutable, meaning that their attributes cannot be modified once assigned.

class DataIngestionConfig:: This line defines a class named DataIngestionConfig. This class represents the configuration for data ingestion in the text summarization project.

root_dir: Path: This line declares an attribute root_dir of type Path within the DataIngestionConfig class. It represents the root directory path for data ingestion.

source_URL: str: This line declares an attribute source_URL of type str within the DataIngestionConfig class. It represents the source URL for the data.

local_data_file: Path: This line declares an attribute local_data_file of type Path within the DataIngestionConfig class. It represents the local data file path.

unzip_dir: Path: This line declares an attribute unzip_dir of type Path within the DataIngestionConfig class. It represents the directory path for unzipping the data.

The subsequent code blocks define similar classes (DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, and ModelEvaluationConfig) with their respective attributes. Each class represents a specific configuration aspect of the text summarization project, such as data validation, data transformation, model training, and model evaluation. The attributes within each class represent the specific configuration settings related to that aspect.

@dataclass(frozen=True): This line is a decorator that indicates that the following class is a data class. The frozen=True argument makes instances of the class immutable, meaning that their attributes cannot be modified once assigned.

class DataValidationConfig:: This line defines a class named DataValidationConfig. This class represents the configuration for data validation in the text summarization project.

root_dir: Path: This line declares an attribute root_dir of type Path within the DataValidationConfig class. It represents the root directory path for data validation.

STATUS_FILE: str: This line declares an attribute STATUS_FILE of type str within the DataValidationConfig class. It represents the file path for the status file related to data validation.

ALL_REQUIRED_FILES: list: This line declares an attribute ALL_REQUIRED_FILES of type list within the DataValidationConfig class. It represents a list of required files for data validation.

The subsequent code blocks (DataTransformationConfig, ModelTrainerConfig, and ModelEvaluationConfig) follow a similar pattern. They define classes with specific configuration settings for data transformation, model training, and model evaluation. Each class has its own attributes representing the respective configuration parameters.

These classes provide a structured way to store and access the various configuration settings required for different aspects of the text summarization project. By using data classes, it becomes easier to create instances of these classes and access their attributes in a straightforward manner.

@dataclass(frozen=True): This line is a decorator that indicates that the following class is a data class. The frozen=True argument makes instances of the class immutable, meaning that their attributes cannot be modified once assigned.

class DataTransformationConfig:: This line defines a class named DataTransformationConfig. This class represents the configuration for data transformation in the text summarization project.

root_dir: Path: This line declares an attribute root_dir of type Path within the DataTransformationConfig class. It represents the root directory path for data transformation.

data_path: Path: This line declares an attribute data_path of type Path within the DataTransformationConfig class. It represents the path to the data used for transformation.

tokenizer_name: Path: This line declares an attribute tokenizer_name of type Path within the DataTransformationConfig class. It represents the name or path of the tokenizer used for data transformation.

The subsequent code blocks (ModelTrainerConfig and ModelEvaluationConfig) continue the pattern of defining classes with specific configuration settings. They represent the configuration for model training and model evaluation, respectively. These classes have various attributes representing parameters such as the root directory, data path, model checkpoint, training epochs, batch size, etc.

By using data classes, the code provides a structured and convenient way to store and access the configuration settings for different components of the text summarization project. It enhances readability and maintainability by grouping related parameters within dedicated classes.

@dataclass(frozen=True): This line is a decorator that indicates that the following class is a data class. The frozen=True argument makes instances of the class immutable, meaning that their attributes cannot be modified once assigned.

class ModelTrainerConfig:: This line defines a class named ModelTrainerConfig. This class represents the configuration for the model training process in the text summarization project.

root_dir: Path: This line declares an attribute root_dir of type Path within the ModelTrainerConfig class. It represents the root directory path for the model trainer.

data_path: Path: This line declares an attribute data_path of type Path within the ModelTrainerConfig class. It represents the path to the data used for model training.

model_ckpt: Path: This line declares an attribute model_ckpt of type Path within the ModelTrainerConfig class. It represents the path to the model checkpoint used for training.

The ModelTrainerConfig class also includes additional attributes related to the training process, such as the number of training epochs, warmup steps, batch size, weight decay, logging steps, evaluation strategy, and so on. These attributes define various parameters and settings for training the model.

The final code block is:

python
 
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    tokenizer_path: Path
    metric_file_name:
This code block defines the ModelEvaluationConfig class, which represents the configuration for model evaluation in the text summarization project. It includes attributes such as the root directory path, data path, model path, tokenizer path, and the metric file name. These attributes store the necessary information for evaluating the trained model.

By using data classes, the code organizes and encapsulates the configuration settings into separate classes, making it easier to manage and access the required parameters for different stages of the text summarization project.

"""