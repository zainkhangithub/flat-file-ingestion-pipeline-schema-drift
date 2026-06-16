from pathlib import Path
import yaml
import pandas as pd


MAPPING_DIR = Path("mappings")


def load_mapping(version):
    mapping_file = MAPPING_DIR / f"{version}_mapping.yaml"

    with open(mapping_file, "r") as f:
        mapping = yaml.safe_load(f)

    return mapping


def standardize_columns(df, version):
    mapping = load_mapping(version)

    df = df.rename(columns=mapping)

    return df