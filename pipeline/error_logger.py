from pathlib import Path
from datetime import datetime
import pandas as pd

from pipeline.config import load_config

config = load_config()

ERROR_LOG_FILE = Path(config["logs"]["error"])
ERROR_LOG_FILE.parent.mkdir(parents=True, exist_ok=True)


def write_error_log(
    file_name,
    error_type,
    error_message
):
    record = {
        "timestamp": datetime.now().isoformat(),
        "file_name": file_name,
        "error_type": error_type,
        "error_message": error_message
    }

    df_new = pd.DataFrame([record])

    if ERROR_LOG_FILE.exists() and ERROR_LOG_FILE.stat().st_size > 0:
        df_existing = pd.read_csv(ERROR_LOG_FILE)
        df_combined = pd.concat(
            [df_existing, df_new],
            ignore_index=True
        )
    else:
        df_combined = df_new

    df_combined.to_csv(ERROR_LOG_FILE, index=False)