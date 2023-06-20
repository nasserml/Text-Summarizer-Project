""" 
This Python code is a part of the machine learning project for text summarization. It evaluates the performance of a text summarization model using the ROUGE metric. Here's a summary of the code:

The code begins by importing necessary libraries and modules such as AutoModelForSeq2SeqLM and AutoTokenizer from the Transformers library, load_dataset, load_from_disk, and load_metric from the Datasets library, as well as torch, pandas, and tqdm.

Next, the code defines a class called ModelEvaluation, which takes a configuration object of type ModelEvaluationConfig as input during initialization.

Inside the ModelEvaluation class, there are three main methods:

generate_batch_sized_chunks: This method splits a given list of elements into smaller batches of a specified size. It uses a generator to yield successive batch-sized chunks.

calculate_metric_on_test_ds: This method calculates the evaluation metric (ROUGE score) on a test dataset. It takes the dataset, metric, model, tokenizer, and other parameters as input. It splits the dataset into smaller batches using the generate_batch_sized_chunks method. It then generates summaries for each batch using the model and tokenizer. The generated summaries are decoded, cleaned, and added to the metric for evaluation. Finally, it computes and returns the ROUGE scores.

evaluate: This method performs the overall evaluation process. It checks the availability of a CUDA device, initializes the tokenizer and the Pegasus model, and loads the test dataset. It also defines a list of ROUGE names and loads the ROUGE metric. It calls the calculate_metric_on_test_ds method to get the ROUGE scores for a subset of the test dataset. The scores are stored in a dictionary and then saved to a CSV file using pandas.

The main purpose of this code is to evaluate the performance of a text summarization model and store the ROUGE scores for further analysis.

"""

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk, load_metric
import torch
import pandas as pd
from tqdm import tqdm
from textSummarizer.entity import ModelEvaluationConfig




class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config


    
    def generate_batch_sized_chunks(self,list_of_elements, batch_size):
        """split the dataset into smaller batches that we can process simultaneously
        Yield successive batch-sized chunks from list_of_elements."""
        for i in range(0, len(list_of_elements), batch_size):
            yield list_of_elements[i : i + batch_size]

    
    def calculate_metric_on_test_ds(self,dataset, metric, model, tokenizer, 
                               batch_size=16, device="cuda" if torch.cuda.is_available() else "cpu", 
                               column_text="article", 
                               column_summary="highlights"):
        article_batches = list(self.generate_batch_sized_chunks(dataset[column_text], batch_size))
        target_batches = list(self.generate_batch_sized_chunks(dataset[column_summary], batch_size))

        for article_batch, target_batch in tqdm(
            zip(article_batches, target_batches), total=len(article_batches)):
            
            inputs = tokenizer(article_batch, max_length=1024,  truncation=True, 
                            padding="max_length", return_tensors="pt")
            
            summaries = model.generate(input_ids=inputs["input_ids"].to(device),
                            attention_mask=inputs["attention_mask"].to(device), 
                            length_penalty=0.8, num_beams=8, max_length=128)
            ''' parameter for length penalty ensures that the model does not generate sequences that are too long. '''
            
            # Finally, we decode the generated texts, 
            # replace the  token, and add the decoded texts with the references to the metric.
            decoded_summaries = [tokenizer.decode(s, skip_special_tokens=True, 
                                    clean_up_tokenization_spaces=True) 
                for s in summaries]      
            
            decoded_summaries = [d.replace("", " ") for d in decoded_summaries]
            
            
            metric.add_batch(predictions=decoded_summaries, references=target_batch)
            
        #  Finally compute and return the ROUGE scores.
        score = metric.compute()
        return score


    def evaluate(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path).to(device)
       
        #loading data 
        dataset_samsum_pt = load_from_disk(self.config.data_path)


        rouge_names = ["rouge1", "rouge2", "rougeL", "rougeLsum"]
  
        rouge_metric = load_metric('rouge')

        score = self.calculate_metric_on_test_ds(
        dataset_samsum_pt['test'][0:10], rouge_metric, model_pegasus, tokenizer, batch_size = 2, column_text = 'dialogue', column_summary= 'summary'
            )

        rouge_dict = dict((rn, score[rn].mid.fmeasure ) for rn in rouge_names )

        df = pd.DataFrame(rouge_dict, index = ['pegasus'] )
        df.to_csv(self.config.metric_file_name, index=False)
        

""" 
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer: Importing the AutoModelForSeq2SeqLM and AutoTokenizer classes from the Transformers library, which are used for sequence-to-sequence language modeling.

from datasets import load_dataset, load_from_disk, load_metric: Importing functions load_dataset, load_from_disk, and load_metric from the Datasets library. These functions are used for loading datasets and metrics.

import torch: Importing the PyTorch library for deep learning.

import pandas as pd: Importing the pandas library for data manipulation and analysis.

from tqdm import tqdm: Importing the tqdm library, which provides a progress bar for loops.

from textSummarizer.entity import ModelEvaluationConfig: Importing the ModelEvaluationConfig class from the textSummarizer.entity module.

class ModelEvaluation:: Defining a class named ModelEvaluation.

def __init__(self, config: ModelEvaluationConfig):: Defining the constructor of the ModelEvaluation class, which takes a ModelEvaluationConfig object as a parameter.

self.config = config: Assigning the input config object to the config attribute of the class instance.

def generate_batch_sized_chunks(self, list_of_elements, batch_size):: Defining a method named generate_batch_sized_chunks that takes a list of elements and a batch size as parameters.

for i in range(0, len(list_of_elements), batch_size):: Starting a loop that iterates over the range from 0 to the length of list_of_elements, incrementing by batch_size in each iteration.

yield list_of_elements[i: i + batch_size]: Yielding a batch-sized chunk of elements from list_of_elements in each iteration.

def calculate_metric_on_test_ds(self, dataset, metric, model, tokenizer, batch_size=16, device="cuda" if torch.cuda.is_available() else "cpu", column_text="article", column_summary="highlights"):: Defining a method named calculate_metric_on_test_ds that takes a dataset, a metric, a model, a tokenizer, and other optional parameters as input.

article_batches = list(self.generate_batch_sized_chunks(dataset[column_text], batch_size)): Splitting the dataset's column_text into smaller batches using the generate_batch_sized_chunks method and storing the result in article_batches.

target_batches = list(self.generate_batch_sized_chunks(dataset[column_summary], batch_size)): Splitting the dataset's column_summary into smaller batches using the generate_batch_sized_chunks method and storing the result in target_batches.

for article_batch, target_batch in tqdm(zip(article_batches, target_batches), total=len(article_batches)):: Looping over the article_batches and target_batches simultaneously using zip and displaying a progress bar using tqdm.

inputs = tokenizer(article_batch, max_length=1024, truncation=True, padding="max_length", return_tensors="pt"): Tokenizing the article_batch using the tokenizer with specified parameters and returning the tokenized tensors.

summaries = model.generate(input_ids=inputs["input_ids"].to(device), attention_mask=inputs["attention_mask"].to(device), length_penalty=0.8, num_beams=8, max_length=128): Generating summaries using the model by passing the input tensors and specifying generation parameters such as length_penalty, num_beams, and max_length.

decoded_summaries = [tokenizer.decode(s, skip_special_tokens=True, clean_up_tokenization_spaces=True) for s in summaries]: Decoding the generated summaries using the tokenizer and removing special tokens.

decoded_summaries = [d.replace("", " ") for d in decoded_summaries]: Replacing any empty strings in the decoded summaries with spaces.

metric.add_batch(predictions=decoded_summaries, references=target_batch): Adding the decoded summaries and target summaries to the metric for evaluation.

score = metric.compute(): Computing the ROUGE scores using the metric.

return score: Returning the computed ROUGE scores.

def evaluate(self):: Defining a method named evaluate within the ModelEvaluation class.

device = "cuda" if torch.cuda.is_available() else "cpu": Assigning the device as "cuda" if a CUDA GPU is available; otherwise, "cpu".

tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path): Initializing the tokenizer using the AutoTokenizer class with the tokenizer path specified in the configuration.

model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path).to(device): Initializing the Pegasus model using the AutoModelForSeq2SeqLM class with the model path specified in the configuration, and moving the model to the specified device.

dataset_samsum_pt = load_from_disk(self.config.data_path): Loading the dataset from the disk using the load_from_disk function with the data path specified in the configuration.

rouge_names = ["rouge1", "rouge2", "rougeL", "rougeLsum"]: Creating a list of ROUGE metric names.

rouge_metric = load_metric('rouge'): Loading the ROUGE metric using the load_metric function with the "rouge" metric name.

score = self.calculate_metric_on_test_ds(dataset_samsum_pt['test'][0:10], rouge_metric, model_pegasus, tokenizer, batch_size=2, column_text='dialogue', column_summary='summary'): Calling the calculate_metric_on_test_ds method with a subset of the test dataset, the ROUGE metric, the Pegasus model, the tokenizer, and other specified parameters. Storing the result in the score variable.

rouge_dict = dict((rn, score[rn].mid.fmeasure) for rn in rouge_names): Creating a dictionary of ROUGE names and their corresponding F-measure scores from the score variable.

df = pd.DataFrame(rouge_dict, index=['pegasus']): Creating a pandas DataFrame from the rouge_dict with 'pegasus' as the index.

df.to_csv(self.config.metric_file_name, index=False): Saving the DataFrame to a CSV file with the filename specified in the configuration.



"""