from src.parser.parse_url import Parser
from src.logging.logger import get_logger


logger = get_logger()


def main_parser():
    """
    Main function to parse images from URLs using the Parser class.

    Returns:
        Parser: The Parser instance used for parsing and saving images.
    """
    logger.info("Parse images from urls")
    parser = Parser()
    parser.save_images()

    return parser
