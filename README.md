# End to end Text-Summarizer-Project

## Workflows

1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src config
5. update the conponents
6. update the pipeline
7. update the main.py
8. update the app.py


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/End-to-end-Text-Summarization
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n summary python=3.8 -y
```

```bash
conda activate summary
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


```bash
Author: Krish Naik
Data Scientist
Email: krishnaik06@gmail.com

```



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/text-s

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app

# End-to-End Text Summarizer Project

This repository contains an end-to-end text summarization project. The project aims to build a text summarization system using machine learning techniques.

## Project Structure

- [`.github/workflows/main.yaml`](.github/workflows/main.yaml): GitHub Actions workflow file for continuous integration and continuous delivery.
- [`config/config.yaml`](config/config.yaml): Configuration file for the project.
- `research/`: Directory containing Jupyter Notebook files for various research and experimentation stages.
  - [`01_data_ingestion.ipynb`](research/01_data_ingestion.ipynb): Notebook for data ingestion.
  - [`02_data_validation.ipynb`](research/02_data_validation.ipynb): Notebook for data validation.
  - [`03_data_transformation.ipynb`](research/03_data_transformation.ipynb): Notebook for data transformation.
  - [`04_model_trainer.ipynb`](research/04_model_trainer.ipynb): Notebook for model training.
  - [`05_model_evaluation.ipynb`](research/05_model_evaluation.ipynb): Notebook for model evaluation.
  - [`Text_Summarization.ipynb`](research/Text_Summarization.ipynb): Main notebook for the text summarization process.
  - [`trails.ipynb`](research/trails.ipynb): Miscellaneous notebook for experimentation and trails.
- `src/textSummarizer/`: Directory containing the source code of the text summarizer.
  - `components/`: Directory for different components of the text summarizer.
    - [`data_ingestion.py`](src/textSummarizer/components/data_ingestion.py): Module for data ingestion.
    - [`data_transformation.py`](src/textSummarizer/components/data_transformation.py): Module for data transformation.
    - [`data_validation.py`](src/textSummarizer/components/data_validation.py): Module for data validation.
    - [`model_evaluation.py`](src/textSummarizer/components/model_evaluation.py): Module for model evaluation.
    - [`model_trainer.py`](src/textSummarizer/components/model_trainer.py): Module for model training.
  - `config/`: Directory for configuration related modules.
    - [`configuration.py`](src/textSummarizer/config/configuration.py): Configuration module.
  - `constants/`: Directory for constant variables.
    - `entity/`: Directory for entity-related constants.
    - `logging/`: Directory for logging-related constants.
    - `pipeline/`: Directory for pipeline-related constants.
  - [`prediction.py`](src/textSummarizer/prediction.py): Module for making predictions using the trained model.
  - [`stage_01_data_ingestion.py`](src/textSummarizer/stage_01_data_ingestion.py): Stage 1 script for data ingestion.
  - [`stage_02_data_validation.py`](src/textSummarizer/stage_02_data_validation.py): Stage 2 script for data validation.
  - [`stage_03_data_transformation.py`](src/textSummarizer/stage_03_data_transformation.py): Stage 3 script for data transformation.
  - [`stage_04_model_trainer.py`](src/textSummarizer/stage_04_model_trainer.py): Stage 4 script for model training.
  - [`stage_05_model_evaluation.py`](src/textSummarizer/stage_05_model_evaluation.py): Stage 5 script for model evaluation.
  - `utils/`: Directory for utility modules.
    - [`common.py`](src/textSummarizer/utils/common.py): Common utility module.
  - `swagger/`: Directory for Swagger related files.
- [`.gitignore`](.gitignore): Git ignore file to specify files and directories that should be ignored by Git.
- [`Dockerfile`](Dockerfile): Dockerfile for containerizing the application.
- [`LICENSE`](LICENSE): License file for the project.
- [`README.md`](README.md): This README file.
- [`app.py`](app.py): Main application file.
- [`main.py`](main.py): Main script to run the application.
- [`params.yaml`](params.yaml): YAML file for specifying parameters.
- [`requirements.txt`](requirements.txt): List of Python dependencies required for the project.
- [`setup.py`](setup.py): Setup script for packaging the project.

