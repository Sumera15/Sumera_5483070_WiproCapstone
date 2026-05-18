import logging
import os


log_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "logs",
    "automation.log"
)

logger = logging.getLogger()

logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(log_path)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def log_message(message):

    logger.info(message)