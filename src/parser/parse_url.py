import requests
import os
from bs4 import BeautifulSoup
from tqdm import tqdm

from src.config.config import config, date_today
from src.logging.logger import get_logger


logger = get_logger()


class Parser:
    """
    A class for parsing web pages, retrieving image links, and saving images.

    Attributes:
        url_list (list): List of URLs to be processed.
        html_content (list): List of HTML content retrieved from the URLs.
        image_groups (list): List of lists containing image links.

    Methods:
        read_urls():
            Read a list of URLs from a file and store them in self.url_list.

        get_html_content():
            Retrieve HTML content from the URLs in self.url_list and store it in self.html_content.

        retrieve_image_links():
            Parse HTML content to retrieve image links and store them in self.image_groups.

        save_images():
            Save images from the retrieved image links to the specified directory.
    """

    def __init__(self):
        """
        Initialize the Parser object.
        """
        self.url_list = None
        self.html_content = None
        self.image_groups = None

        self.read_urls()
        self.get_html_content()
        self.retrieve_image_links()

    def read_urls(self):
        """
        Read a list of URLs from a file and store them in self.url_list.
        """
        logger.info("--- Read urls")

        with open(config["url_data_dir"]) as f:
            self.url_list = f.read().splitlines()

    def get_html_content(self):
        """
        Retrieve HTML content from the URLs in self.url_list and store it in self.html_content.
        """
        logger.info("--- Getting html content")

        url_list = self.url_list
        self.html_content = []

        for url in url_list:
            response = requests.get(url)
            self.html_content.append(response.text)

    def retrieve_image_links(self):
        """
        Parse HTML content to retrieve image links and store them in self.image_groups.
        """
        logger.info("--- Retrieving image links")

        self.image_groups = []

        for html_content in self.html_content:
            soup = BeautifulSoup(html_content, 'html.parser')
            image_tags = soup.find_all('img')

            image_urls = [img['src'] for img in image_tags if 'src' in img.attrs]
            self.image_groups.append(image_urls)

    def save_images(self):
        """
        Save images from the retrieved image links to the specified directory.

        Returns:
            int: The number of saved images.
        """
        logger.info("--- Saving images:")

        save_directory = config['save_images_dir']
        os.makedirs(save_directory, exist_ok=True)

        image_n = 0
        image_urls = [item for sublist in self.image_groups for item in sublist]

        for image_url in tqdm(image_urls, desc=f"{date_today.strftime('%d/%m/%Y %H:%M:%S')} INFO"):
            response = requests.get("http:" + image_url)
            with open(os.path.join(save_directory, f'train_{image_n}.jpg'), 'wb') as file:
                file.write(response.content)
                image_n += 1

        logger.info("--- Number of saving images = {}".format(image_n))
