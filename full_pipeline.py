from src.parser.main_parser import main_parser
from src.dataset.main_dataset import main_dataset
from src.logging.logger import init_logger, get_logger
from src.config.config import config


if __name__ == "__main__":
    init_logger()
    logger = get_logger()

    if config["parse"]:
        parser = main_parser()

    train_dataset = main_dataset()
