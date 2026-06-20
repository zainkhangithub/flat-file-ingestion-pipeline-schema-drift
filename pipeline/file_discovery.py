from pathlib import Path

from pipeline.config import load_config

config = load_config()

INCOMING_DIR = Path(config["paths"]["incoming"])
PROCESSED_DIR = Path(config["paths"]["processed"])
FAILED_DIR = Path(config["paths"]["failed"])


def discover_files():
    """
    Only returns files that have not already been processed or failed.
    """

    processed_files = {f.name for f in PROCESSED_DIR.glob("*.txt")}
    failed_files = {f.name for f in FAILED_DIR.glob("*.txt")}

    excluded = processed_files.union(failed_files)

    files = []

    for file in INCOMING_DIR.glob("*.txt"):
        if file.name not in excluded:
            files.append(file)

    return files