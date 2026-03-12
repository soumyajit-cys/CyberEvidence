import sqlite3
from config import REPORT_FILE, DATABASE_PATH

def generate_report():

    conn = sqlite3.connect(DATABASE_PATH)

    files = conn.execute("SELECT * FROM files LIMIT 20").fetchall()
    logs = conn.execute("SELECT * FROM logs").fetchall()
    network = conn.execute("SELECT * FROM network").fetchall()

    html = "<h1>Digital Forensics Investigation Report</h1>"

    html += "<h2>Files</h2>"
    html += str(files)

    html += "<h2>Logs</h2>"
    html += str(logs)

    html += "<h2>Network</h2>"
    html += str(network)

    with open(REPORT_FILE,"w") as f:
        f.write(html)