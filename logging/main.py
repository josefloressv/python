# Example how to use the logging module
"""
The logging module is part of the Python standard library and provides tracking for events that occur while software runs.
You can use it to output log messages to different outputs, such as the console or a file.
Lelvels:
- DEBUG = 10 (Detailed information, typically of interest only when diagnosing problems)
- INFO = 20 (Confirmation that things are working as expected)
- WARNING = 30 (An indication that something unexpected happened, or indicative of some problem in the near future)
- ERROR = 40 (Due to a more serious problem, the software has not been able to perform some function)
- CRITICAL = 50 (A serious error, indicating that the program itself may be unable to continue running)
"""
import logging

# Create a logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) # Set the logger level to the lowest level to capture all messages

# Create a console handler for DEBUG, INFO, and WARNING messages
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # Set the level to DEBUG to capture all messages up to WARNING

# Create a file handler for ERROR and CRITICAL messages
file_handler = logging.FileHandler('error.log')
file_handler.setLevel(logging.ERROR)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add the formatter to the file handler
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add both handler to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Log some messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
