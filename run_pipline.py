"""
run_pipeline.py - Master ETL Pipeline
"""
import subprocess
import sys

scripts = [
    "scripts/data_ingestion.py",
    "scripts/data_cleaning.py",
    "scripts/load_database.py",
    "scripts/live_nav_fetch.py",
    "scripts/run_queries.py",
]

for script in scripts:
    print(f"\nRunning {script}...")
    result = subprocess.run(
        [sys.executable, script],
        capture_output=True, text=True)
    if result.returncode == 0:
        print(f"DONE: {script}")
    else:
        print(f"ERROR in {script}:")
        print(result.stderr)

print("\nPipeline complete!")