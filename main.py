from pipeline.orchestrator import run_pipeline


result = run_pipeline("raw/tests_data/test_2025_missing_col.txt")

print("\nDRIFT STATUS:")
print(result["drift_status"])

print("\nMISSING:")
print(result["missing_cols"])

print("\nNEW:")
print(result["new_cols"])