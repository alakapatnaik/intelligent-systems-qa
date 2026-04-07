from loguru import logger
from pathlib import Path 
import logging
import os
from datetime import datetime

# create log directory if not exists
os.makedirs("log", exist_ok = True)

# log file name with timestamp
log_filename = f"logs/test_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

# create logger
def get_logger(name:str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # format
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt = "%Y-%m-%d %H:%M:%S"
    )

    # console handler - prints to terminal
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # file handler - saves to log file
    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # add handlers
    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger







LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logger.add(LOG_DIR / "test_run.log" , rotation="1 MB", retention = "10 days")

__all__ = ["logger"]