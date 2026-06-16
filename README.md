# Flat File Ingestion Pipeline (Schema Drift Handling)

## Overview

This project implements a lightweight ETL pipeline for processing evolving government flat files. It handles schema drift using detection, canonical mapping, validation, and audit logging.

The system is designed to be:
- Schema-aware (version-based detection)
- Drift-tolerant (supports non-breaking changes)
- Validation-driven (enforces required fields)
- Observable (audit logging for traceability)

---

## Architecture Diagram
            ┌──────────────────────┐
            │     RAW FILES        │
            │ (Gov Flat Files)     │
            └─────────┬────────────┘
                      │
                      ▼
            ┌──────────────────────┐
            │  SCHEMA DETECTION    │
            │  (Best Match)        │
            └─────────┬────────────┘
                      │
                      ▼
            ┌──────────────────────┐
            │ CANONICAL MAPPING    │
            │ (Normalize Columns)  │
            └─────────┬────────────┘
                      │
                      ▼
            ┌──────────────────────┐
            │   VALIDATION         │
            │ (Drift Detection)    │
            │ - Missing Fields     │
            │ - Extra Fields       │
            └─────────┬────────────┘
                      │
                      ▼
            ┌──────────────────────┐
            │  AUDIT LOGGING       │
            │ (CSV History)        │
            └──────────────────────┘


---

## Folder Structure

# flat-file-ingestion-pipeline-schema-drift/
```
flat-file-ingestion-pipeline-schema-drift/
│
├── raw/                        # Input government files
├── schemas/                    # Schema definitions
│   ├── 2024.yaml
│   ├── 2025.yaml
│   └── canonical_schema.yaml
│
├── mappings/                   # Column mapping rules
│   ├── 2024_mapping.yaml
│   └── 2025_mapping.yaml
│
├── pipeline/
│   ├── context.py
│   ├── detect_schema.py
│   ├── transform.py
│   ├── validate.py
│   ├── logger.py
│   └── orchestrator.py
│
├── tests_data/                 # Sample datasets for testing
├── run_tests.py                # Automated test runner
├── main.py                     # Entry point
│
└── logs/
    └── pipeline_log.csv        # Audit logs
```

## Core Components

### 1. Schema Detection
- Identifies the closest matching schema version
- Uses column overlap scoring
- Avoids strict equality matching

---

### 2. Canonical Mapping
- Converts source columns into a unified schema
- Ensures downstream logic is stable across years

Example:

| Source Column   | Canonical Column |
|----------------|------------------|
| fname          | first_name       |
| lname          | last_name        |
| zip            | zip_code         |

---

### 3. Validation Layer
Handles:
- Required column checks
- Detection of new columns
- Drift classification

### Drift Types

| Type         | Meaning |
|--------------|--------|
| NO_DRIFT     | Schema matches expected structure |
| NON_BREAKING | Extra columns added |
| BREAKING     | Required columns missing |

---

### 4. Orchestrator
- Controls full pipeline execution
- Coordinates all modules
- Returns structured results

---

### 5. Audit Logging
Stores execution metadata in:

Includes:
- timestamp
- file name
- schema version
- row count
- drift status
- missing columns
- new columns

---

## Running the Pipeline

### Run Main Pipeline
```bash
python main.py
```

### Run Test Suite
```bash
python run_tests.py
```

### Expected output:
```bash
clean   => NO_DRIFT
extra   => NON_BREAKING
missing => BREAKING
```