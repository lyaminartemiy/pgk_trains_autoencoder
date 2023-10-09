from datetime import datetime
from pathlib import Path


date_today = datetime.today()
date_str = f"{date_today.year}{date_today.month}{date_today.day}_{date_today.hour}_{date_today.minute}"


config = dict(
    url_data_dir="data/url/urls.txt",
    save_images_dir="data/images",

    PATH_LOGS=Path("./logs/"),
    LOG_FILE=f"log_{date_str}.log"
)