import logging
from pathlib import Path
from src.config.config import config


LOGGER_NAME = 'model_log'


def init_logger(log_level_for_console: str = "info", log_level_for_file: str = "debug"):
    """
    Initialize a logger with specified log levels for console and file output.

    Args:
        log_level_for_console (str): Log level for console output (default: "info").
        log_level_for_file (str): Log level for file output (default: "debug").
    """
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(level=logging.DEBUG)
    logger.propagate = False

    formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s", "%d/%m/%Y %H:%M:%S")

    ch = logging.StreamHandler()
    ch.setLevel(log_level_for_console.upper())
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    path = Path(config["PATH_LOGS"])
    path.mkdir(parents=True, exist_ok=True)

    fh = logging.FileHandler(path.joinpath(config["LOG_FILE"]), mode="w")
    fh.setLevel(log_level_for_file.upper())
    fh.setFormatter(formatter)
    logger.addHandler(fh)


def get_logger():
    """
    Get the initialized logger.

    Returns:
        logging.Logger: The logger instance.
    """
    return logging.getLogger(LOGGER_NAME)
