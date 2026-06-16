import pandas as pd

from pipeline.detect_schema import detect_schema
from pipeline.transform import standardize_columns
from pipeline.validate import (
    load_canonical_schema,
    validate_required_columns,
    detect_new_columns,
    classify_drift
)
from pipeline.logger import write_audit_log
from pipeline.context import PipelineContext


def run_pipeline(file_path):
    schema = detect_schema(file_path)

    if not schema:
        raise Exception("Unknown schema detected!")

    df = pd.read_csv(file_path, delimiter=schema["delimiter"])

    context = PipelineContext(file_path, schema, df)

    # Transform
    df_std = standardize_columns(df, context.version)
    context.df = df_std

    # Validate
    canonical_schema = load_canonical_schema()

    missing_cols = validate_required_columns(df_std, canonical_schema)
    new_cols = detect_new_columns(df_std, canonical_schema)

    drift_status = classify_drift(missing_cols, new_cols)

    # Log
    write_audit_log(
        file_name=file_path,
        schema_version=context.version,
        row_count=len(df_std),
        drift_status=drift_status,
        missing_cols=missing_cols,
        new_cols=new_cols
    )

    return {
        "context": context,
        "drift_status": drift_status,
        "missing_cols": missing_cols,
        "new_cols": new_cols
    }