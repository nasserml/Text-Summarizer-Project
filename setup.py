import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "nasserml"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "mnasserone@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)

""" 
import setuptools: Imports the setuptools module, which is used for packaging Python projects.

with open("README.md", "r", encoding="utf-8") as f: ...: Opens the "README.md" file in read mode and assigns the file object to the variable f. The file is read with UTF-8 encoding.

long_description = f.read(): Reads the contents of the "README.md" file and assigns it to the variable long_description.

__version__ = "0.0.0": Defines a variable __version__ with the initial value of "0.0.0", representing the version of the package.

REPO_NAME = "Text-Summarizer-Project": Defines a variable REPO_NAME with the value "Text-Summarizer-Project", representing the name of the GitHub repository.

AUTHOR_USER_NAME = "nasserml": Defines a variable AUTHOR_USER_NAME with the value "nasserml", representing the author's GitHub username.

SRC_REPO = "textSummarizer": Defines a variable SRC_REPO with the value "textSummarizer", representing the name of the source repository.

AUTHOR_EMAIL = "mnasserone@gmail.com": Defines a variable AUTHOR_EMAIL with the author's email address.

setuptools.setup(...):

Begins the setup configuration for the package using setuptools.
Specifies various package metadata such as name, version, author, author email, and description.
Sets the long description for the package using the content read from "README.md".
Specifies the format of the long description as "text/markdown".
Specifies the URL and project URLs associated with the package, including a bug tracker URL.
Sets the package directory to "src".
Uses setuptools.find_packages() to automatically find and include all packages within the "src" directory.
This code is a typical setup script for a Python package. It defines the package metadata, including the package name, version, author details, description, and project URLs. It also specifies the package directory and includes all packages within the "src" directory. The long description is set from the contents of the "README.md" file.
"""