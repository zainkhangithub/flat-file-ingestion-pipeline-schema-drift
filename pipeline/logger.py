from pathlib import Path
import pandas as pd
from datetime import datetime


LOG_FILE = Path("logs/pipeline_log.csv")


def write_audit_log(
    file_name,
    schema_version,
    row_count,
    drift_status,
    missing_cols,
    new_cols
):
    record = {
        "timestamp": datetime.now().isoformat(),
        "file_name": file_name,
        "schema_version": schema_version,
        "row_count": row_count,
        "drift_status": drift_status,
        "missing_columns": ",".join(missing_cols),
        "new_columns": ",".join(new_cols)
    }

    df_new = pd.DataFrame([record])

    if LOG_FILE.exists() and LOG_FILE.stat().st_size > 0:
        df_existing = pd.read_csv(LOG_FILE)
        df_combined = pd.concat(
            [df_existing, df_new],
            ignore_index=True
        )
    else:
        df_combined = df_new

    df_combined.to_csv(LOG_FILE, index=False)