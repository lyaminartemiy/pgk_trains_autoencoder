from src.parser.main_parser import main_parser
from src.logging.logger import init_logger, get_logger


if __name__ == "__main__":
    init_logger()
    logger = get_logger()

    parser = main_parser()
