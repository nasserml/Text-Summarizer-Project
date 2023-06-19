
""" 
The provided code performs data transformation for the text summarization project. Here's a summary of the code:

- It imports the necessary modules and classes: `os`, `logger` from `textSummarizer.logging`, `AutoTokenizer` from `transformers`, `load_dataset` and `load_from_disk` from `datasets`, and `DataTransformationConfig` from `textSummarizer.entity`.

- The `DataTransformation` class is defined. It has an `__init__` method that initializes the instance with a `config` parameter of type `DataTransformationConfig`. It also creates an `AutoTokenizer` instance based on the tokenizer name specified in the configuration.

- The `convert_examples_to_features` method takes an `example_batch` as input and performs tokenization on the dialogue and summary parts using the tokenizer. It returns a dictionary containing the input IDs, attention mask, and labels.

- The `convert` method loads the dataset from disk using the data path specified in the configuration. It then maps the `convert_examples_to_features` method to the dataset, converting examples to features in batches. Finally, it saves the transformed dataset to disk at the specified path.

In summary, this code provides the functionality to transform data by tokenizing dialogue and summary text and saving the transformed dataset for the text summarization project.

"""
import os
from textSummarizer.entity import DataTransformationConfig
from textSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)


    
    def convert_examples_to_features(self,example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'] , max_length = 1024, truncation = True )
        
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length = 128, truncation = True )
            
        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    

    def convert(self):
        dataset_samsum = load_from_disk(self.config.data_path)
        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched = True)
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir,"samsum_dataset"))
        
"""
import os: This line imports the os module, which provides functions for interacting with the operating system.

from textSummarizer.logging import logger: This line imports the logger object from the textSummarizer.logging module. It is used for logging purposes.

from transformers import AutoTokenizer: This line imports the AutoTokenizer class from the transformers module. It is used for tokenization.

from datasets import load_dataset, load_from_disk: This line imports the load_dataset and load_from_disk functions from the datasets module. They are used for loading datasets.

from textSummarizer.entity import DataTransformationConfig: This line imports the DataTransformationConfig class from the textSummarizer.entity module. It represents the configuration for data transformation.

class DataTransformation: This line defines the DataTransformation class.

def __init__(self, config: DataTransformationConfig): This line defines the constructor (__init__) of the DataTransformation class, which takes a config parameter of type DataTransformationConfig. It initializes the instance by assigning the config to the self.config attribute. It also creates an instance of AutoTokenizer based on the tokenizer name specified in the configuration and assigns it to the self.tokenizer attribute.

def convert_examples_to_features(self, example_batch): This line defines the convert_examples_to_features method of the DataTransformation class. It takes an example_batch as input. Inside the method, it uses the tokenizer to tokenize the dialogue and summary parts of the example batch. It returns a dictionary containing the input IDs, attention mask, and labels.

def convert(self): This line defines the convert method of the DataTransformation class. It performs the data transformation process. It loads the dataset from disk using the data path specified in the configuration. Then, it maps the convert_examples_to_features method to the dataset, converting examples to features in batches. Finally, it saves the transformed dataset to disk at the specified path.

dataset_samsum = load_from_disk(self.config.data_path): This line loads the dataset from disk using the data path specified in the configuration and assigns it to the dataset_samsum variable.

dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched=True): This line applies the convert_examples_to_features method to the dataset_samsum dataset, converting examples to features in batches. The result is assigned to the dataset_samsum_pt variable.

dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir, "samsum_dataset")): This line saves the transformed dataset to disk at the path specified by joining the root directory and the "samsum_dataset" directory name.

In summary, this code defines a DataTransformation class that performs data transformation by tokenizing dialogue and summary text and saves the transformed dataset to disk.
"""
