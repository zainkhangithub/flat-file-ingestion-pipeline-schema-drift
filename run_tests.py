from pathlib import Path
from pipeline.orchestrator import run_pipeline


TEST_DATA = "raw/tests_data/"

TEST_FILES = {
    "clean": TEST_DATA + "test_2025_clean.txt",
    "extra": TEST_DATA + "test_2025_extra_col.txt",
    "missing": TEST_DATA + "test_2025_missing_col.txt"
}

expected = {
    "clean": "NO_DRIFT",
    "extra": "NON_BREAKING",
    "missing": "BREAKING"
}

results = {}

for name, file_path in TEST_FILES.items():
    print(f"\nRunning test: {name}")

    output = run_pipeline(str(file_path))

    results[name] = output["drift_status"]

    print("Result:", output["drift_status"])

print("\n--- SUMMARY ---")
for k in results:
    print(k, "=>", results[k], "| expected:", expected[k])