""" 
from textSummarizer.config.configuration import ConfigurationManager: Imports the ConfigurationManager class from the textSummarizer.config.configuration module.

from transformers import AutoTokenizer: Imports the AutoTokenizer class from the transformers module.

from transformers import pipeline: Imports the pipeline function from the transformers module.

class PredictionPipeline:: Defines a class named PredictionPipeline.

def __init__(self):: Defines the constructor method for the PredictionPipeline class.

self.config = ConfigurationManager().get_model_evaluation_config(): Creates an instance of the ConfigurationManager class, retrieves the model evaluation configuration using the get_model_evaluation_config() method, and assigns it to the config variable of the PredictionPipeline instance.

def predict(self, text):: Defines a method named predict within the PredictionPipeline class that takes a text parameter.

tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path): Creates an instance of the AutoTokenizer class using the tokenizer path specified in the configuration and assigns it to the tokenizer variable.

gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}: Creates a dictionary gen_kwargs that contains the generation arguments for the summarization task.

pipe = pipeline("summarization", model=self.config.model_path, tokenizer=tokenizer): Creates a summarization pipeline using the pipeline function with the task type set to "summarization", the model path specified in the configuration, and the tokenizer instance.

print("Dialogue:"): Prints the string "Dialogue:".

print(text): Prints the value of the text parameter.

output = pipe(text, **gen_kwargs)[0]["summary_text"]: Generates a summary using the pipe pipeline with the input text and the generation arguments specified in gen_kwargs. The generated summary is extracted from the pipeline output and assigned to the output variable.

print("\nModel Summary:"): Prints the string "Model Summary:".

print(output): Prints the value of the output variable.

return output: Returns the generated summary.

In summary, this code defines a PredictionPipeline class that uses the model evaluation configuration to generate summaries for input texts. It initializes the pipeline with the necessary components, such as the tokenizer and model, and provides a predict method to generate a summary for a given text input.

"""

from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()


    
    def predict(self,text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}

        pipe = pipeline("summarization", model=self.config.model_path,tokenizer=tokenizer)

        print("Dialogue:")
        print(text)

        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)

        return output