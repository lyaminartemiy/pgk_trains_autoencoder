from datetime import datetime
from pathlib import Path

import torch.cuda

date_today = datetime.today()
date_str = f"{date_today.year}{date_today.month}{date_today.day}_{date_today.hour}_{date_today.minute}"

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'


config = dict(
    url_data_dir="data/url/urls.txt",
    save_images_dir="../data/images",

    PATH_LOGS=Path("./logs/"),
    LOG_FILE=f"log_{date_str}.log",

    parse=False,

    RESCALE_SIZE=64,
    LATENT_SIZE=16,

    MAX_EPOCHS=20,
    BATCH_SIZE=4,

    DEVICE=DEVICE,
)
