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

The project structure is organized as follows:

- `.github/workflows`: Contains the GitHub Actions workflow configuration files.
  - [main.yaml](.github/workflows/main.yaml): Workflow file for Continuous Integration and Continuous Delivery.

- `config`: Contains configuration files for the project.
  - [config.yaml](config/config.yaml): Configuration file for the project.

- `research`: Contains Jupyter notebooks related to data analysis and experimentation.
  - [01_data_ingestion.ipynb](research/01_data_ingestion.ipynb): Notebook for data ingestion.
  - [02_data_validation.ipynb](research/02_data_validation.ipynb): Notebook for data validation.
  - [03_data_transformation.ipynb](research/03_data_transformation.ipynb): Notebook for data transformation.
  - [04_model_trainer.ipynb](research/04_model_trainer.ipynb): Notebook for model training.
  - [05_model_evaluation.ipynb](research/05_model_evaluation.ipynb): Notebook for model evaluation.
  - [Text_Summarization.ipynb](research/Text_Summarization.ipynb): Main notebook for text summarization.

- `src/textSummarizer`: Contains the source code for the text summarizer.
  - `components`: Contains the components of the text summarizer.
    - [__init__.py](src/textSummarizer/components/__init__.py): Initialization file for the components module.
    - [data_ingestion.py](src/textSummarizer/components/data_ingestion.py): Module for data ingestion.
    - [data_transformation.py](src/textSummarizer/components/data_transformation.py): Module for data transformation.
    - [data_validation.py](src/textSummarizer/components/data_validation.py): Module for data validation.
    - [model_evaluation.py](src/textSummarizer/components/model_evaluation.py): Module for model evaluation.
    - [model_trainer.py](src/textSummarizer/components/model_trainer.py): Module for model training.

  - `config`: Contains the configuration files for the text summarizer.
    - [__init__.py](src/textSummarizer/config/__init__.py): Initialization file for the config module.
    - [configuration.py](src/textSummarizer/config/configuration.py): Module for configuration settings.

  - `constants`: Contains constant values used in the text summarizer.
    - [__init__.py](src/textSummarizer/constants/__init__.py): Initialization file for the constants module.

  - `entity`: Contains entity classes used in the text summarizer.
    - [__init__.py](src/textSummarizer/entity/__init__.py): Initialization file for the entity module.

  - `logging`: Contains modules related to logging.
    - [__init__.py](src/textSummarizer/logging/__init__.py): Initialization file for the logging module.

  - `pipeline`: Contains the pipeline modules for text summarization.
    - [__init__.py](src/textSummarizer/pipeline/__init__.py): Initialization file for the pipeline module.
    - [prediction.py](src/textSummarizer/pipeline/prediction.py): Module for text summarization predictions.

  - [stage_01_data_ingestion.py](src/textSummarizer/stage_01_data_ingestion.py): Script for stage 1 - data ingestion.
  - [stage_02_data_validation.py](src/textSummarizer/stage_02_data_validation.py): Script for stage 2 - data validation.
  - [stage_03_data_transformation.py](src/textSummarizer/stage_03_data_transformation.py): Script for stage 3 - data transformation.
  - [stage_04_model_trainer.py](src/textSummarizer/stage_04_model_trainer.py): Script for stage 4 - model training.
  - [stage_05_model_evaluation.py](src/textSummarizer/stage_05_model_evaluation.py): Script for stage 5 - model evaluation.

  - `utils`: Contains utility modules used in the text summarizer.
    - [__init__.py](src/textSummarizer/utils/__init__.py): Initialization file for the utils module.
    - [common.py](src/textSummarizer/utils/common.py): Module for common utility functions.

- `swagger`: Contains Swagger API documentation files.

- [.gitignore](.gitignore): Specifies the files and directories to be ignored by Git.
- [Dockerfile](Dockerfile): Dockerfile for building the project into a Docker container.
- [LICENSE](LICENSE): License file for the project.
- [README.md](README.md): This file, providing an overview of the project.
- [app.py](app.py): Main application script.
- [main.py](main.py): Main script for running the application.
- [params.yaml](params.yaml): Parameters file for the project.
- [requirements.txt](requirements.txt): Python dependencies required by the project.
- [setup.py](setup.py): Setup file for the project.
- [template.py](template.py): Template file for the project.
- [test.py](test.py): Test file for the project.


## Getting Started

To get started with the project, follow the instructions below:

1. Clone the repository: `git clone https://github.com/your-username/your-repo.git`
2. Install the dependencies: `pip install -r requirements.txt`
3. Configure the project parameters in `params.yaml`.
4. Run the application: `python main.py`
5. Access the text summarization API at `http://localhost:8080`.

## License

This project is licensed under the [MIT License](LICENSE).

