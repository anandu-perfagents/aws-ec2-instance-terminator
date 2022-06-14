from logging import Logger

import sys
import logging


# Creates a logger file to keep track of EC2 instance activity
logger: Logger = logging.getLogger(
    "POC SCRIPT"
)  # Set logger name to identify the script
file_handler = logging.FileHandler(
    "poc_logger.log"
)  # To store the log int a file with name `poc_logger.log`.

console_handler = logging.StreamHandler(
    sys.stdout
)  # also get the log in console and standard std out pipe.

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s : %(message)s"
)  # format to log the output

console_handler.setFormatter(formatter)  # Apply formster to console
file_handler.setFormatter(formatter)  # Apply formater to file
logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
