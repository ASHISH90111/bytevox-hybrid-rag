import sqlite3
from datetime import datetime

from app.config import LOG_DB


def initialize_database():

    conn = sqlite3.connect(LOG_DB)

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS query_logs (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp TEXT,

            question TEXT,

            answer TEXT,

            sources TEXT,

            latency REAL

        )
        """
    )

    conn.commit()

    conn.close()


def log_query(
    question,
    answer,
    sources,
    latency
):

    conn = sqlite3.connect(LOG_DB)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO query_logs
        (
            timestamp,
            question,
            answer,
            sources,
            latency
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            question,
            answer,
            ", ".join(sources),
            latency
        )
    )

    conn.commit()

    conn.close()