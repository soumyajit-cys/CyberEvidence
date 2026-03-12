import sqlite3
from config import DATABASE_PATH

class DBManager:

    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_PATH)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS files(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            path TEXT,
            hash TEXT,
            size INTEGER,
            modified TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            event_type TEXT,
            source TEXT,
            description TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS network(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            src_ip TEXT,
            dst_ip TEXT,
            protocol TEXT,
            length INTEGER
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS metadata(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file TEXT,
            camera TEXT,
            timestamp TEXT,
            gps TEXT
        )
        """)

        self.conn.commit()

    def insert(self, query, data):
        self.cursor.execute(query, data)
        self.conn.commit()

    def fetch(self, query):
        return self.cursor.execute(query).fetchall()