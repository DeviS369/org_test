import logging
import os
from datetime import datetime

# Create a logger instance
def setup_logger(name, log_file="test_execution.log", level=logging.INFO):
    """
    Sets up a logger with the given name, log file, and level.

    Args:
        name (str): Name of the logger.
        log_file (str): Path to the log file.
        level (int): Logging level (e.g., logging.INFO, logging.DEBUG).
    Returns:
        logger: Configured logger instance.
    """
    # Create logs directory if it doesn't exist
    logs_dir = "./logs"
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    # Format the log messages
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    # Configure the logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create a file handler to write logs to a file
    file_handler = logging.FileHandler(os.path.join(logs_dir, log_file))
    file_handler.setFormatter(logging.Formatter(log_format, date_format))

    # Create a stream handler to display logs in the console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(log_format, date_format))

    # Add handlers to the logger
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger


# Example Usage
if __name__ == "__main__":
    logger = setup_logger("TestLogger", log_file="test_execution.log", level=logging.DEBUG)
    logger.info("This is an informational message.")
    logger.debug("This is a debug message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical error message.")
