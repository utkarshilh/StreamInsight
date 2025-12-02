import csv
import psycopg2
import os

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

CSV_FILE = "contents.csv"


def main():
    if not os.path.exists(CSV_FILE):
        print(f"{CSV_FILE} does not exist.")
        return

    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    if not rows:
        print("No data to insert.")
        return

    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

    curr = conn.cursor()

    insert_sql = """
    INSERT INTO contents (name, type, no_of_seasons, runtime_min, episodes, platform, created_at)
    VALUES (%s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP)
    ON CONFLICT (name, platform) DO NOTHING;
    """

    inserted = 0

    for row in rows:
        data = (
            row.get("name"),
            row.get("type"),
            row.get("seasons"),
            row.get("runtime"),
            row.get("episodes"),
            row.get("platform")
        )

        curr.execute(insert_sql, data)
        inserted += 1

    conn.commit()
    curr.close()
    conn.close()

    print(f"Data insertion completed. Total inserted: {inserted}")

    # Clear CSV after successful insertion
    open(CSV_FILE, "w").close()
    print("CSV cleared.")


if __name__ == "__main__":
    main()
