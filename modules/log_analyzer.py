from database.db_manager import DBManager

db = DBManager()

def analyze_auth_log():

    try:
        with open("/var/log/auth.log") as f:

            for line in f:

                if "Failed password" in line:

                    db.insert_log((
                        "Unknown",
                        "Failed Login",
                        "auth.log",
                        line.strip()
                    ))

                if "sudo" in line:

                    db.insert_log((
                        "Unknown",
                        "Sudo Activity",
                        "auth.log",
                        line.strip()
                    ))
    except:
        pass