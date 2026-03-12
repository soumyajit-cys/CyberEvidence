import os
import hashlib
from database.db_manager import DBManager

db = DBManager()

def hash_file(path):

    sha256 = hashlib.sha256()

    try:
        with open(path,"rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)

        return sha256.hexdigest()

    except:
        return None


def analyze_file(path):

    try:

        size = os.path.getsize(path)
        modified = os.path.getmtime(path)

        file_hash = hash_file(path)

        db.insert(
        "INSERT INTO files(name,path,hash,size,modified) VALUES(?,?,?,?,?)",
        (
            os.path.basename(path),
            path,
            file_hash,
            size,
            str(modified)
        ))

    except:
        pass