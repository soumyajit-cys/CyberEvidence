from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db():

    conn = sqlite3.connect("database/evidence.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/dashboard")
def dashboard():

    db = get_db()

    files = db.execute("SELECT COUNT(*) FROM files").fetchone()[0]
    logs = db.execute("SELECT COUNT(*) FROM logs").fetchone()[0]
    network = db.execute("SELECT COUNT(*) FROM network").fetchone()[0]

    return render_template(
        "dashboard.html",
        files=files,
        logs=logs,
        network=network
    )


@app.route("/files")
def files():

    db = get_db()
    data = db.execute("SELECT * FROM files").fetchall()

    return render_template("files.html",data=data)


@app.route("/logs")
def logs():

    db = get_db()
    data = db.execute("SELECT * FROM logs").fetchall()

    return render_template("logs.html",data=data)


@app.route("/network")
def network():

    db = get_db()
    data = db.execute("SELECT * FROM network").fetchall()

    return render_template("network.html",data=data)


if __name__ == "__main__":
    app.run(debug=True)