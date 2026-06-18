from pathlib import Path

INCOMING_DIR = Path("incoming")
PROCESSED_DIR = Path("processed")
FAILED_DIR = Path("failed")


def discover_files():
    """
    Only returns files that are still in incoming/.
    Ensures idempotent processing.
    """

    processed_files = {f.name for f in PROCESSED_DIR.glob("*.txt")}
    failed_files = {f.name for f in FAILED_DIR.glob("*.txt")}

    excluded = processed_files.union(failed_files)

    files = []

    for file in INCOMING_DIR.glob("*.txt"):
        if file.name not in excluded:
            files.append(file)

    return files