from src.logging.logger import get_logger
from src.dataset.create_dataset import TrainsDataset
from src.dataset.process.transforms import train_transforms


logger = get_logger()


def main_dataset() -> TrainsDataset:
    """

    :return:
    """
    logger.info("Create dataset to NN")
    dataset = TrainsDataset(train_transforms)

    return dataset
