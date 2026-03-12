from database.db_manager import DBManager

db = DBManager()

def analyze_logs():

    try:

        with open("/var/log/auth.log") as f:

            for line in f:

                if "Failed password" in line:

                    db.insert(
                    "INSERT INTO logs(timestamp,event_type,source,description) VALUES(?,?,?,?)",
                    (
                        "unknown",
                        "Failed Login",
                        "auth.log",
                        line.strip()
                    ))

                if "sudo" in line:

                    db.insert(
                    "INSERT INTO logs(timestamp,event_type,source,description) VALUES(?,?,?,?)",
                    (
                        "unknown",
                        "Sudo Activity",
                        "auth.log",
                        line.strip()
                    ))

    except:
        pass