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
            file_id INTEGER PRIMARY KEY,
            file_name TEXT,
            file_path TEXT,
            file_hash TEXT,
            file_size INTEGER,
            modified_date TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs(
            event_id INTEGER PRIMARY KEY,
            timestamp TEXT,
            event_type TEXT,
            source TEXT,
            description TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS network(
            packet_id INTEGER PRIMARY KEY,
            source_ip TEXT,
            destination_ip TEXT,
            protocol TEXT,
            packet_length INTEGER
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS metadata(
            file_name TEXT,
            camera_model TEXT,
            timestamp TEXT,
            gps_location TEXT
        )
        """)

        self.conn.commit()

    def insert_file(self, data):
        self.cursor.execute(
        "INSERT INTO files(file_name,file_path,file_hash,file_size,modified_date) VALUES(?,?,?,?,?)", data)
        self.conn.commit()

    def insert_log(self,data):
        self.cursor.execute(
        "INSERT INTO logs(timestamp,event_type,source,description) VALUES(?,?,?,?)", data)
        self.conn.commit()

    def insert_network(self,data):
        self.cursor.execute(
        "INSERT INTO network(source_ip,destination_ip,protocol,packet_length) VALUES(?,?,?,?)", data)
        self.conn.commit()

    def insert_metadata(self,data):
        self.cursor.execute(
        "INSERT INTO metadata VALUES(?,?,?,?)", data)
        self.conn.commit()