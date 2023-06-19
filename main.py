""" 
The code represents the main script that executes a series of pipeline stages for training a text summarization model.

Import statements: Import the necessary pipeline classes (DataIngestionTrainingPipeline, DataValidationTrainingPipeline, etc.) from their respective modules, as well as the logger object from the textSummarizer.logging module.

STAGE_NAME = "Data Ingestion stage": Defines a constant variable STAGE_NAME with the value "Data Ingestion stage".

Execution block for Data Ingestion stage: Executes the data ingestion stage of the pipeline. It starts by logging a stage start message, creates an instance of the DataIngestionTrainingPipeline class, and calls its main method. After the stage is completed, it logs a stage completion message.

Execution block for Data Validation stage: Executes the data validation stage of the pipeline. Similar to the previous block, it starts by logging a stage start message, creates an instance of the DataValidationTrainingPipeline class, and calls its main method. After the stage is completed, it logs a stage completion message.

Execution block for Data Transformation stage: Executes the data transformation stage of the pipeline. Again, it starts by logging a stage start message, creates an instance of the DataTransformationTrainingPipeline class, and calls its main method. After the stage is completed, it logs a stage completion message.

Execution block for Model Trainer stage: Executes the model training stage of the pipeline. It logs a separator line, a stage start message, creates an instance of the ModelTrainerTrainingPipeline class, and calls its main method. After the stage is completed, it logs a stage completion message.

Execution block for Model Evaluation stage: Executes the model evaluation stage of the pipeline. It logs a separator line, a stage start message, creates an instance of the ModelEvaluationTrainingPipeline class, and calls its main method. After the stage is completed, it logs a stage completion message.

In summary, this code executes multiple pipeline stages in sequence, including data ingestion, data validation, data transformation, model training, and model evaluation. Each stage is encapsulated in a separate pipeline class, and the main script orchestrates the execution of these stages by creating instances of the respective classes and calling their main methods. Logging messages are used to indicate the start and completion of each stage, and any exceptions that occur are logged and re-raised.

"""

from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.logging import logger


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
    
    

""" 
Import statements: Import the necessary pipeline classes (DataIngestionTrainingPipeline, DataValidationTrainingPipeline, etc.) from their respective modules, as well as the logger object from the textSummarizer.logging module.
3-8: Define and execute the "Data Ingestion stage" of the pipeline:

Define the constant variable STAGE_NAME with the value "Data Ingestion stage".
Use a try block to handle any exceptions that may occur during the execution of this stage.
Log a message indicating the start of the stage using the logger.info() method.
Create an instance of the DataIngestionTrainingPipeline class and assign it to the data_ingestion variable.
Call the main() method of the data_ingestion object to execute the data ingestion stage.
Log a message indicating the completion of the stage using the logger.info() method.
If an exception occurs during the execution, log the exception using the logger.exception() method and re-raise it.
10-20: Repeat the same pattern for the "Data Validation stage", "Data Transformation stage", "Model Trainer stage", and "Model Evaluation stage".

Update the STAGE_NAME variable accordingly.
Log stage start and completion messages specific to each stage.
Create an instance of the corresponding pipeline class (DataValidationTrainingPipeline, DataTransformationTrainingPipeline, etc.).
Call the main() method of the pipeline object.
Handle any exceptions that occur during the execution of each stage.
In summary, this code represents the main script for running a text summarization training pipeline. It sequentially executes different stages of the pipeline, such as data ingestion, data validation, data transformation, model training, and model evaluation. Each stage is encapsulated in a separate pipeline class, and the script creates instances of these classes to execute the stages. Logging messages are used to indicate the start and completion of each stage, and any exceptions that occur during execution are logged and re-raised.

"""