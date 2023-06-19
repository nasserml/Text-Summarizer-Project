""" 
Sure! Here's a summary of the provided Python code:

The code sets up a data ingestion pipeline for training a text summarization model.

1. `from textSummarizer.config.configuration import ConfigurationManager`: Imports the `ConfigurationManager` class from the `textSummarizer.config.configuration` module. This class is responsible for managing the configuration settings for the pipeline.

2. `from textSummarizer.conponents.data_ingestion import DataIngestion`: Imports the `DataIngestion` class from the `textSummarizer.conponents.data_ingestion` module. This class handles the downloading and extraction of data.

3. `from textSummarizer.logging import logger`: Imports the `logger` object from the `textSummarizer.logging` module. It is assumed that the `logger` object is responsible for logging messages.

5. `class DataIngestionTrainingPipeline:`: Defines a class named `DataIngestionTrainingPipeline` that represents the data ingestion pipeline.

7. `def __init__(self):`: Defines the initialization method for the `DataIngestionTrainingPipeline` class.

9. `pass`: Indicates that the initialization method does not contain any additional code.

12. `def main(self):`: Defines a method named `main` within the `DataIngestionTrainingPipeline` class. This method serves as the entry point for the pipeline.

14. `config = ConfigurationManager()`: Creates an instance of the `ConfigurationManager` class and assigns it to the `config` variable.

15. `data_ingestion_config = config.get_data_ingestion_config()`: Retrieves the data ingestion configuration using the `get_data_ingestion_config` method of the `ConfigurationManager` class and assigns it to the `data_ingestion_config` variable.

16. `data_ingestion = DataIngestion(config=data_ingestion_config)`: Creates an instance of the `DataIngestion` class, passing the `data_ingestion_config` as the configuration parameter, and assigns it to the `data_ingestion` variable.

17. `data_ingestion.download_file()`: Calls the `download_file` method of the `DataIngestion` instance to download the required data file.

18. `data_ingestion.extract_zip_file()`: Calls the `extract_zip_file` method of the `DataIngestion` instance to extract the contents of the downloaded zip file.

In summary, this code sets up a data ingestion pipeline by utilizing the `ConfigurationManager` to obtain the data ingestion configuration. It then creates an instance of the `DataIngestion` class, which is responsible for downloading and extracting the required data. The pipeline's entry point is the `main` method, which orchestrates the execution of the data ingestion process.

"""

from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.logging import logger


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()