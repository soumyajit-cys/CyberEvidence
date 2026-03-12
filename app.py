from flask import Flask, render_template
import sqlite3
from config import DATABASE_PATH

app = Flask(__name__,template_folder="dashboard/templates")

def db():

    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/dashboard")
def dashboard():

    database = db()

    files = database.execute("SELECT COUNT(*) FROM files").fetchone()[0]
    logs = database.execute("SELECT COUNT(*) FROM logs").fetchone()[0]
    network = database.execute("SELECT COUNT(*) FROM network").fetchone()[0]
    metadata = database.execute("SELECT COUNT(*) FROM metadata").fetchone()[0]

    return render_template("dashboard.html",
                           files=files,
                           logs=logs,
                           network=network,
                           metadata=metadata)

@app.route("/files")
def files():

    database = db()
    data = database.execute("SELECT * FROM files LIMIT 50").fetchall()

    return render_template("files.html",data=data)

@app.route("/logs")
def logs():

    database = db()
    data = database.execute("SELECT * FROM logs").fetchall()

    return render_template("logs.html",data=data)

@app.route("/network")
def network():

    database = db()
    data = database.execute("SELECT * FROM network").fetchall()

    return render_template("network.html",data=data)

@app.route("/metadata")
def metadata():

    database = db()
    data = database.execute("SELECT * FROM metadata").fetchall()

    return render_template("metadata.html",data=data)

if __name__ == "__main__":
    app.run(debug=True)