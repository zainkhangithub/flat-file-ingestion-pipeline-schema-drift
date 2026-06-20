from pipeline.file_discovery import discover_files
from pipeline.orchestrator import run_pipeline
from pipeline.file_manager import move_to_processed, move_to_failed
from pipeline.error_logger import write_error_log
from pipeline.exceptions import (
    SchemaDetectionError,
    ValidationError,
    FileFormatError
)

def process_batch():
    files = discover_files()

    results = []

    for file_path in files:
        file_path = str(file_path)

        print(f"\nProcessing: {file_path}")

        try:
            result = run_pipeline(file_path)

            new_location = move_to_processed(file_path)

            results.append({
                "file": file_path,
                "status": "SUCCESS",
                "drift_status": result["drift_status"],
                "moved_to": new_location
            })

        except SchemaDetectionError as e:
            
            write_error_log(
                file_name=file_path,
                error_type="SCHEMA_DETECTION_ERROR",
                error_message=str(e)
            )

            new_location = move_to_failed(file_path)

            results.append({
                "file": file_path,
                "status": "FAILED",
                "error_type": "SCHEMA_DETECTION_ERROR",
                "error_message": str(e),
                "moved_to": new_location
            })

        except ValidationError as e:
            
            write_error_log(
                file_name=file_path,
                error_type="VALIDATION_ERROR",
                error_message=str(e)
            )

            new_location = move_to_failed(file_path)

            results.append({
                "file": file_path,
                "status": "FAILED",
                "error_type": "VALIDATION_ERROR",
                "error_message": str(e),
                "moved_to": new_location
            })

        except FileFormatError as e:
            
            write_error_log(
                file_name=file_path,
                error_type="FILE_FORMAT_ERROR",
                error_message=str(e)
            )

            new_location = move_to_failed(file_path)

            results.append({
                "file": file_path,
                "status": "FAILED",
                "error_type": "FILE_FORMAT_ERROR",
                "error_message": str(e),
                "moved_to": new_location
            })

        except Exception as e:

            write_error_log(
                file_name=file_path,
                error_type="SYSTEM_ERROR",
                error_message=str(e)
            )

            new_location = move_to_failed(file_path)

            results.append({
                "file": file_path,
                "status": "FAILED",
                "error_type": "SYSTEM_ERROR",
                "error_message": str(e),
                "moved_to": new_location
            })
    return results