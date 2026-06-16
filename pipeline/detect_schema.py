from pathlib import Path
import yaml


SCHEMA_DIR = Path("schemas/source")


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
    actual_columns = set(read_header(file_path))

    schemas = load_schemas()

    best_match = None
    best_score = 0

    for schema in schemas:
        expected = set(schema["columns"])

        score = len(expected.intersection(actual_columns)) / len(expected)

        if score > best_score:
            best_score = score
            best_match = schema

    # IMPORTANT: always return best match (no failure here)
    return best_match