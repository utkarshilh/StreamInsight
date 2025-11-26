import csv
import os

source_file = "Netflix.csv"
target_file = "contents.csv"
default_value = 'netflix'

# Step 1: Read data from source
if os.path.exists(source_file):
    with open(source_file, "r", newline='', encoding='utf-8') as source:
        reader = csv.reader(source)
        data = list(reader)
else:
    data = []

# Step 2: Check if data exists
if len(data) > 0:

    # Step 3: Add default column to each row
    for row in data:
        row.append(default_value)

    # Step 4: Append to target CSV
    with open(target_file, "a", newline='', encoding='utf-8') as target:
        writer = csv.writer(target)
        writer.writerows(data)

    # Step 5: Clear the source file safely
    with open(source_file, "w", newline='', encoding='utf-8') as source:
        source.truncate(0)  # makes sure file is completely emptied

    print(f"Data appended successfully to {target_file} and {source_file} cleared.")

else:
    print("No data found in source file")
