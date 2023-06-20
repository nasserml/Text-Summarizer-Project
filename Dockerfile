FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate

CMD ["python3", "app.py"]



#Let's go through each line of the Dockerfile and understand its purpose:
#
#```dockerfile
#FROM python:3.8-slim-buster
#```
#This line specifies the base image for the Docker container, which is `python:3.8-slim-buster`. It provides a slim version of the Python 3.8 interpreter on the Debian Buster operating system.
#
#```dockerfile
#RUN apt update -y && apt install awscli -y
#```
#This line updates the package list inside the container and installs the AWS Command Line Interface (CLI) using the `apt` package manager. The `-y` flag automatically answers "yes" to any prompts during the installation.
#
#```dockerfile
#WORKDIR /app
#```
#This line sets the working directory for the subsequent instructions to `/app`. It creates a directory named "app" inside the container where the application code will be placed.
#
#```dockerfile
#COPY . /app
#```
#This line copies the contents of the current directory (the context) into the `/app` directory of the container. It ensures that all the files and folders in the current directory are available inside the container.
#
#```dockerfile
#RUN pip install -r requirements.txt
#```
#This line installs the Python dependencies specified in the `requirements.txt` file using `pip`. It assumes that there is a `requirements.txt` file in the current directory, which contains the necessary Python packages and their versions.
#
#```dockerfile
#RUN pip install --upgrade accelerate
#```
#This line upgrades the `accelerate` package, which is a library for optimizing and accelerating PyTorch and TensorFlow models.
#
#```dockerfile
#RUN pip uninstall -y transformers accelerate
#```
#This line uninstalls the `transformers` and `accelerate` packages, if they were previously installed. This step ensures that the Docker container starts with a clean slate and prevents conflicts with any potential previously installed versions.
#
#```dockerfile
#RUN pip install transformers accelerate
#```
#This line installs the `transformers` and `accelerate` packages, ensuring they are installed with their latest versions. These packages are commonly used in natural language processing tasks, such as text summarization.
#
#```dockerfile
#CMD ["python3", "app.py"]
#```
#This line specifies the command that will be executed when the container starts. It runs the `app.py` Python script using the `python3` interpreter. This assumes that there is an `app.py` file in the `/app` directory, which contains the main code for the text summarization project.
#
#Overall, this Dockerfile sets up a container environment based on the Python 3.8-slim-buster image, installs necessary dependencies, and copies the project code. It then installs the required Python packages, sets the working directory, and specifies the command to run the application.