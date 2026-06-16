from pathlib import Path
import yaml


CANONICAL_SCHEMA_PATH = Path("schemas/canonical/canonical_schema.yaml")


def load_canonical_schema():
    with open(CANONICAL_SCHEMA_PATH, "r") as f:
        return yaml.safe_load(f)


def validate_required_columns(df, schema):
    required = set(schema["required_columns"])
    actual = set(df.columns)

    missing = required - actual

    return list(missing)


def detect_new_columns(df, schema):
    allowed = set(schema["required_columns"]) | set(schema["optional_columns"])

    actual = set(df.columns)

    new_columns = actual - allowed

    return list(new_columns)


def classify_drift(missing_cols, new_cols):
    if missing_cols:
        return "BREAKING"

    if new_cols:
        return "NON_BREAKING"

    return "NO_DRIFT"