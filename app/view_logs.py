import sqlite3

from app.config import LOG_DB


def view_logs():

    conn = sqlite3.connect(LOG_DB)

    cursor = conn.cursor()

    rows = cursor.execute(
        """
        SELECT
            id,
            timestamp,
            question,
            answer,
            sources,
            latency
        FROM query_logs
        ORDER BY id DESC
        """
    ).fetchall()

    conn.close()

    print("=" * 100)

    if not rows:
        print("No logs found.")
        return

    for row in rows:

        print(f"Log ID      : {row[0]}")
        print(f"Timestamp   : {row[1]}")
        print(f"Question    : {row[2]}")
        print(f"Answer      : {row[3]}")
        print(f"Sources     : {row[4]}")
        print(f"Latency(ms) : {row[5]}")

        print("-" * 100)


if __name__ == "__main__":

    view_logs()