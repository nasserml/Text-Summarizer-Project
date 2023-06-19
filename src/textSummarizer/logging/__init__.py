""" This code initializes a logging module in Python. It imports the necessary modules, such as os, sys, and logging. It sets up a logging format with a specific string pattern.

The code creates a directory named "logs" if it doesn't already exist, and sets the log file path to "logs/running_logs.log" using the os.path.join() function. It ensures that the directory is created by calling os.makedirs() with the argument exist_ok=True.

The code then configures the logging module using logging.basicConfig(). It sets the logging level to INFO and specifies the format of the log messages using the logging_str string. It also specifies two handlers for the log messages: logging.FileHandler to write log messages to the log file specified by log_filepath, and logging.StreamHandler to print log messages to the console.

Finally, the code creates a logger object named "textSummarizerLogger" using logging.getLogger(), which can be used to log messages in the application. """

import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)



logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("textSummarizerLogger")

""" import os: This line imports the os module, which provides functions for interacting with the operating system.

import sys: This line imports the sys module, which provides access to some variables used or maintained by the interpreter and functions that interact with the interpreter.

import logging: This line imports the logging module, which is a built-in module in Python for logging messages from the application.

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]": This line defines a string format for the log messages. It uses placeholders like %(asctime)s, %(levelname)s, %(module)s, and %(message)s to represent different parts of the log message.

log_dir = "logs": This line assigns the string "logs" to the variable log_dir, which represents the directory where the log file will be stored.

log_filepath = os.path.join(log_dir,"running_logs.log"): This line uses the os.path.join() function to create a file path by combining the log_dir and the file name "running_logs.log". The resulting file path will be stored in the variable log_filepath.

os.makedirs(log_dir, exist_ok=True): This line creates a directory specified by log_dir. If the directory already exists, it does nothing (exist_ok=True). This ensures that the directory exists before attempting to write log files to it.

logging.basicConfig(: This line starts the configuration of the logging module.

level=logging.INFO,: This line sets the logging level to INFO, which means that only log messages with a severity level of INFO and higher will be processed and displayed.

format=logging_str,: This line sets the format of the log messages using the logging_str string defined earlier.

handlers=[: This line starts the definition of the handlers for the log messages.

logging.FileHandler(log_filepath),: This line adds a FileHandler to the handlers list. It specifies that log messages should be written to the file specified by log_filepath.

logging.StreamHandler(sys.stdout): This line adds a StreamHandler to the handlers list. It specifies that log messages should be printed to the console (sys.stdout).

]: This line closes the list of handlers.

): This line closes the logging.basicConfig() function call.

logger = logging.getLogger("textSummarizerLogger"): This line creates a logger object named "textSummarizerLogger" using the getLogger() function from the logging module. The logger object can be used to log messages in the application.
The logger object created in the last line can now be used throughout the code to log messages. For example, you can use logger.debug() to log debug messages, logger.info() for informational messages, logger.warning() for warning messages, and so on.
Overall, this code sets up a logging module in Python with a specific log format and handlers. It creates a directory for log files if it doesn't exist, and configures the logging level and log message format. It also sets up handlers to write log messages to a file and print them to the console. Finally, it creates a logger object that can be used to log messages in the application, named "textSummarizerLogger" in this case.

"""