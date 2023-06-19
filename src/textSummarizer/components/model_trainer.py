""" 
The provided Python code defines a class named `ModelTrainer` within the module `model_trainer.py` for a text summarization task in a machine learning project. Here is a summary of the code:

- The necessary imports include modules from the `transformers` library, such as `TrainingArguments`, `Trainer`, `DataCollatorForSeq2Seq`, `AutoModelForSeq2SeqLM`, and `AutoTokenizer`. Additionally, the code imports `load_dataset` and `load_from_disk` functions from the `datasets` module, as well as `torch` and `os` modules.

- The `ModelTrainer` class is defined, which takes a `config` object of type `ModelTrainerConfig` as input during initialization.

- The `train` method is defined within the `ModelTrainer` class. It performs the training process for the text summarization model.

- The code first checks if a CUDA device is available and assigns the device as "cuda" if it is, otherwise "cpu". It then initializes the tokenizer and model for sequence-to-sequence generation using the `AutoTokenizer` and `AutoModelForSeq2SeqLM` classes from the `transformers` library, based on the provided `model_ckpt` attribute in the `config` object.

- A `DataCollatorForSeq2Seq` object is created, which handles the data collation process during training.

- The code loads the dataset from disk using the `load_from_disk` function and the specified data path from the `config` object.

- Training arguments, such as the output directory, number of epochs, batch sizes, logging and evaluation steps, and gradient accumulation steps, are set using the `TrainingArguments` class from the `transformers` library. Alternatively, there is commented-out code that shows a more customizable approach to setting the training arguments.

- A `Trainer` object is created with the initialized model, training arguments, tokenizer, data collator, and the loaded train and validation datasets.

- The `trainer.train()` method is called to start the training process.

- After training, the trained model and tokenizer are saved to the specified directories using the `save_pretrained` method.

This code represents a specific implementation of the text summarization model training process, utilizing the Pegasus architecture.

"""

from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
from textSummarizer.entity import ModelTrainerConfig
import torch
import os


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config


    
    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)
        
        #loading data 
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        # trainer_args = TrainingArguments(
        #     output_dir=self.config.root_dir, num_train_epochs=self.config.num_train_epochs, warmup_steps=self.config.warmup_steps,
        #     per_device_train_batch_size=self.config.per_device_train_batch_size, per_device_eval_batch_size=self.config.per_device_train_batch_size,
        #     weight_decay=self.config.weight_decay, logging_steps=self.config.logging_steps,
        #     evaluation_strategy=self.config.evaluation_strategy, eval_steps=self.config.eval_steps, save_steps=1e6,
        #     gradient_accumulation_steps=self.config.gradient_accumulation_steps
        # ) 


        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir, num_train_epochs=1, warmup_steps=500,
            per_device_train_batch_size=1, per_device_eval_batch_size=1,
            weight_decay=0.01, logging_steps=10,
            evaluation_strategy='steps', eval_steps=500, save_steps=1e6,
            gradient_accumulation_steps=16
        ) 

        trainer = Trainer(model=model_pegasus, args=trainer_args,
                  tokenizer=tokenizer, data_collator=seq2seq_data_collator,
                  train_dataset=dataset_samsum_pt["test"], 
                  eval_dataset=dataset_samsum_pt["validation"])
        
        trainer.train()

        ## Save model
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir,"pegasus-samsum-model"))
        ## Save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))
        

""" 

1. `from transformers import TrainingArguments, Trainer`: Imports the `TrainingArguments` and `Trainer` classes from the `transformers` library. These classes are used for configuring and executing the training process.

2. `from transformers import DataCollatorForSeq2Seq`: Imports the `DataCollatorForSeq2Seq` class from the `transformers` library. This class is responsible for collating data during training for sequence-to-sequence tasks.

3. `from transformers import AutoModelForSeq2SeqLM, AutoTokenizer`: Imports the `AutoModelForSeq2SeqLM` and `AutoTokenizer` classes from the `transformers` library. These classes are used for initializing the model and tokenizer for sequence-to-sequence generation.

4. `from datasets import load_dataset, load_from_disk`: Imports the `load_dataset` and `load_from_disk` functions from the `datasets` library. These functions are used for loading datasets during training.

5. `from textSummarizer.entity import ModelTrainerConfig`: Imports the `ModelTrainerConfig` class from the `textSummarizer.entity` module. This class represents the configuration for the model trainer.

6. `import torch`: Imports the `torch` module, which is a popular machine learning framework.

7. `import os`: Imports the `os` module, which provides functions for interacting with the operating system.

9. `class ModelTrainer:`: Defines a class named `ModelTrainer`.

10. `def __init__(self, config: ModelTrainerConfig):`: Defines the initialization method for the `ModelTrainer` class. It takes a `config` object of type `ModelTrainerConfig` as input.

12. `self.config = config`: Assigns the `config` input to the `config` attribute of the `ModelTrainer` instance.

15. `def train(self):`: Defines the `train` method within the `ModelTrainer` class. This method performs the training process.

17. `device = "cuda" if torch.cuda.is_available() else "cpu"`: Checks if a CUDA device is available and assigns the `device` variable as "cuda" if available, otherwise "cpu". This determines the device on which the model will be trained.

18. `tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)`: Initializes the tokenizer using the `AutoTokenizer` class from the `transformers` library. It loads the tokenizer from the specified `model_ckpt` attribute in the `config` object.

19. `model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)`: Initializes the model using the `AutoModelForSeq2SeqLM` class from the `transformers` library. It loads the model from the specified `model_ckpt` attribute in the `config` object and moves it to the selected device.

20. `seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)`: Initializes the data collator for sequence-to-sequence tasks using the `DataCollatorForSeq2Seq` class from the `transformers` library. It takes the tokenizer and the model as input.

23. `dataset_samsum_pt = load_from_disk(self.config.data_path)`: Loads the dataset from disk using the `load_from_disk` function from the `datasets` library. It uses the specified `data_path` attribute in the `config` object.

28. `trainer_args = TrainingArguments(...)`: Defines the training arguments using the `TrainingArguments` class from the `transformers` library.

 The arguments include settings for the output directory, number of training epochs, batch sizes, logging and evaluation steps, and gradient accumulation steps. The commented-out code provides an alternative, more customizable approach to setting the training arguments.

39. `trainer = Trainer(...)`: Creates a `Trainer` object from the `Trainer` class in the `transformers` library. It takes the initialized model, training arguments, tokenizer, data collator, and the loaded train and validation datasets as inputs.

42. `trainer.train()`: Starts the training process using the `train` method of the `Trainer` object.

45. `model_pegasus.save_pretrained(...)`: Saves the trained model to the specified directory using the `save_pretrained` method of the `model_pegasus` object.

48. `tokenizer.save_pretrained(...)`: Saves the tokenizer to the specified directory using the `save_pretrained` method of the `tokenizer` object.

This code defines a `ModelTrainer` class, initializes the necessary components for training a text summarization model, loads the dataset, configures the training arguments, trains the model using the `Trainer` class, and saves the trained model and tokenizer.
"""