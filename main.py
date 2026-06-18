from pipeline.batch_processor import process_batch

results = process_batch()

print("\n=== BATCH SUMMARY ===")

for result in results:
    print(result)