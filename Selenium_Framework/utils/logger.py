import logging
import os


if not os.path.exists("logs"):

    os.makedirs("logs")


logger = logging.getLogger()

logger.setLevel(logging.INFO)


file_handler = logging.FileHandler(
    "logs/automation.log"
)

console_handler = logging.StreamHandler()


formatter = logging.Formatter(
    "%(asctime)s - %(message)s"
)

file_handler.setFormatter(formatter)

console_handler.setFormatter(formatter)


logger.addHandler(file_handler)

logger.addHandler(console_handler)


def log_message(message):

    logger.info(message)