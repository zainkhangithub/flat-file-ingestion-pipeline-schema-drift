from pathlib import Path
import pandas as pd
from datetime import datetime

from pipeline.config import load_config

config = load_config()

AUDIT_LOG_FILE = Path(config["logs"]["audit"])
AUDIT_LOG_FILE.parent.mkdir(parents=True, exist_ok=True)


def write_audit_log(**record):
    record["timestamp"] = datetime.now().isoformat()

    df_new = pd.DataFrame([record])

    if AUDIT_LOG_FILE.exists() and AUDIT_LOG_FILE.stat().st_size > 0:
        df_existing = pd.read_csv(AUDIT_LOG_FILE)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_combined = df_new

    df_combined.to_csv(AUDIT_LOG_FILE, index=False)