import sqlite3

def generate_report():

    conn = sqlite3.connect("database/evidence.db")

    files = conn.execute("SELECT * FROM files").fetchall()
    logs = conn.execute("SELECT * FROM logs").fetchall()
    network = conn.execute("SELECT * FROM network").fetchall()

    report = open("reports/forensic_report.html","w")

    report.write("<h1>Digital Forensics Investigation Report</h1>")

    report.write("<h2>File Analysis</h2>")
    report.write(str(files))

    report.write("<h2>Log Events</h2>")
    report.write(str(logs))

    report.write("<h2>Network Activity</h2>")
    report.write(str(network))

    report.close()