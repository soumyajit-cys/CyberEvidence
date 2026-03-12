import exifread
from database.db_manager import DBManager
from config import IMAGE_EXTENSIONS

db = DBManager()

def extract_metadata(path):

    if not any(path.lower().endswith(ext) for ext in IMAGE_EXTENSIONS):
        return

    try:

        with open(path,'rb') as f:

            tags = exifread.process_file(f)

            camera = str(tags.get("Image Model","Unknown"))
            timestamp = str(tags.get("EXIF DateTimeOriginal","Unknown"))
            gps = str(tags.get("GPS GPSLatitude","Unknown"))

            db.insert(
            "INSERT INTO metadata(file,camera,timestamp,gps) VALUES(?,?,?,?)",
            (path,camera,timestamp,gps))

    except:
        pass