from pathlib import Path
import shutil

from pipeline.config import load_config

config = load_config()

PROCESSED_DIR = Path(config["paths"]["processed"])
FAILED_DIR = Path(config["paths"]["failed"])


def move_to_processed(file_path):
    dest = PROCESSED_DIR / Path(file_path).name
    shutil.move(file_path, dest)
    return str(dest)


def move_to_failed(file_path):
    dest = FAILED_DIR / Path(file_path).name
    shutil.move(file_path, dest)
    return str(dest)