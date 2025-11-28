import csv
import os
import sys
import traceback

folder = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
source_file = os.path.join(folder, "Netflix.csv")
target_file = os.path.join(folder, "contents.csv")
default_value = 'netflix'

def human_size(path):
    try:
        return f"{os.path.getsize(path)} bytes"
    except OSError:
        return "N/A"

def preview_rows(rows, n=3):
    for i, r in enumerate(rows[:n]):
        print(f"  row {i}: {r}")

try:
    print("Folder:", folder)
    print("Source file:", source_file)
    print("Target file:", target_file)
    print("Source size before:", human_size(source_file))
    print("Target size before:", human_size(target_file))
    print()

    # Guard: ensure source and target are not the same file
    if os.path.abspath(source_file) == os.path.abspath(target_file):
        print("ERROR: source and target are the same file. Aborting.")
        sys.exit(1)

    # Read source
    if os.path.exists(source_file):
        with open(source_file, "r", newline='', encoding='utf-8') as source:
            reader = csv.reader(source)
            data = list(reader)
        print("Rows read from source:", len(data))
        if len(data) > 0:
            print("Preview of first rows:")
            preview_rows(data, n=5)
    else:
        print("Source file does not exist.")
        data = []

    if len(data) == 0:
        print("No data found in source file. Nothing to append or clear.")
        sys.exit(0)

    # Add default column
    for row in data:
        row.append(default_value)

    # Append to target (ensure file exists)
    os.makedirs(os.path.dirname(target_file) or ".", exist_ok=True)
    with open(target_file, "a", newline='', encoding='utf-8') as target:
        writer = csv.writer(target)
        writer.writerows(data)
        # ensure data is flushed to disk
        try:
            target.flush()
            os.fsync(target.fileno())
        except Exception as e:
            # fsync may fail on some platforms/virtual FS, but we still try
            print("Warning: could not fsync target file:", e)

    print("Data appended to target.")

    # Now truncate the source file safely
    # Open for r+ (read/write) to preserve file permissions, then truncate to 0
    with open(source_file, "r+", newline='', encoding='utf-8') as s:
        s.truncate(0)
        try:
            s.flush()
            os.fsync(s.fileno())
        except Exception as e:
            print("Warning: could not fsync source file:", e)

    print("Source file truncated (cleared).")
    print("Source size after:", human_size(source_file))
    print("Target size after:", human_size(target_file))

except Exception as exc:
    print("An error occurred:")
    traceback.print_exc()
    sys.exit(1)
