from pathlib import Path
import yaml


CONFIG_FILE = Path("config/pipeline.yaml")


def load_config():
    with open(CONFIG_FILE, "r") as f:
        return yaml.safe_load(f)