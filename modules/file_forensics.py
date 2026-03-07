import hashlib
import os
from database.db_manager import DBManager

db = DBManager()

def calculate_hash(filepath):

    sha256 = hashlib.sha256()

    try:
        with open(filepath,"rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)

        return sha256.hexdigest()

    except:
        return None


def analyze_file(filepath):

    try:
        file_hash = calculate_hash(filepath)

        file_size = os.path.getsize(filepath)

        modified = os.path.getmtime(filepath)

        data = (
            os.path.basename(filepath),
            filepath,
            file_hash,
            file_size,
            str(modified)
        )

        db.insert_file(data)

    except:
        pass