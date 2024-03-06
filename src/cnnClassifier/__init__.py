import os  # Import the os module for interacting with the operating system
import sys  # Import the sys module for system-specific parameters and functions
import logging  # Import the logging module for logging messages

# Define the logging format string
logging_str ="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define the directory to store logs
log_dir = "logs"

# Define the filepath for the log file
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create the logs directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configure the logging module
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format=logging_str,  # Set the logging format
    handlers=[  # Define the logging handlers
        logging.FileHandler(log_filepath),  # Log messages to a file
        logging.StreamHandler(sys.stdout)  # Print log messages to the console
    ]
)

# Get the logger instance with the specified name
logger = logging.getLogger("cnnClassifierLogger")

