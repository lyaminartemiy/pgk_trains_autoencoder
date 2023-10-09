import os
import numpy as np
from torch.utils.data import Dataset
from torchvision import transforms
from PIL import Image

from src.config.config import config


class TrainsDataset(Dataset):
    """
    Custom dataset for loading and preparing training images.
    """

    def __init__(self, transform: transforms):
        """
        Initialize the TrainsDataset.

        Args:
            transform (transforms.Compose): A composition of image transformations.
        """
        super(TrainsDataset, self).__init__()
        self.transform = transform

    @staticmethod
    def load_sample(image_path):
        """
        Load an image from the specified path.

        Args:
            image_path (str): Path to the image file.

        Returns:
            PIL.Image.Image: The loaded image.
        """
        image = Image.open(image_path)  # .convert('RGB')
        image.load()

        return image

    @staticmethod
    def prepare_sample(image):
        """
        Prepare an image for training.

        Args:
            image (PIL.Image.Image): The image to be prepared.

        Returns:
            PIL.Image.Image: The prepared image.
        """
        image = image.resize((config["RESCALE_SIZE"], config["RESCALE_SIZE"]))
        image = np.array(image)

        return image

    def __getitem__(self, id_image: int):
        """
        Get a training sample by index.

        Args:
            id_image (int): Index of the image.

        Returns:
            torch.Tensor: The processed image tensor.
        """
        file_name = f"train_{id_image}"
        image_path = os.path.join(config["save_images_dir"], file_name)

        image = self.load_sample(image_path)
        image = self.prepare_sample(image)

        image = np.array(image / 255, dtype='float32')
        image = self.transform(image)

        return image

    def __len__(self):
        """
        Get the number of training samples in the dataset.

        Returns:
            int: Number of training samples.
        """
        file_n = len([name for name in os.listdir(config["save_images_dir"]) if os.path.isfile(name)])

        return file_n
