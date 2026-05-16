from pathlib import Path
import yaml


SCHEMA_DIR = Path("schemas")


def load_schemas():
    schemas = []

    for file in SCHEMA_DIR.glob("*.yaml"):
        with open(file, "r") as f:
            schema = yaml.safe_load(f)
            schemas.append(schema)

    return schemas


def read_header(file_path, delimiter="|"):
    with open(file_path, "r") as f:
        first_line = f.readline().strip()

    return first_line.split(delimiter)


def detect_schema(file_path):
    actual_columns = read_header(file_path)

    schemas = load_schemas()

    for schema in schemas:
        expected_columns = schema["columns"]
        if actual_columns == expected_columns:
            return schema

    return None