import pandas as pd

from pipeline.detect_schema import detect_schema
from pipeline.transofrm import standardize_columns
from pipeline.validation import (
    load_canonical_schema,
    validate_required_columns,
    detect_new_columns,
    classify_drift
)


file_path = "raw/2025/citizens.txt"

schema = detect_schema(file_path)

if not schema:
    raise Exception("Unknown schema detected!")

delimiter = schema["delimiter"]
version = schema["version"]

df = pd.read_csv(file_path, delimiter=delimiter)

print("\nORIGINAL DATAFRAME:")
print(df)

df_standardized = standardize_columns(df, version)

print("\nSTANDARDIZED DATAFRAME:")
print(df_standardized)

canonical_schema = load_canonical_schema()

missing_cols = validate_required_columns(
    df_standardized,
    canonical_schema
)

new_cols = detect_new_columns(
    df_standardized,
    canonical_schema
)

drift_status = classify_drift(
    missing_cols,
    new_cols
)

print("\nDRIFT STATUS:")
print(drift_status)

print("\nMISSING COLUMNS:")
print(missing_cols)

print("\nNEW COLUMNS:")
print(new_cols)