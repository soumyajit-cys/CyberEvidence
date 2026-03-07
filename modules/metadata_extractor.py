import exifread
from database.db_manager import DBManager

db = DBManager()

def extract_metadata(image_path):

    try:
        with open(image_path,'rb') as f:

            tags = exifread.process_file(f)

            camera = str(tags.get("Image Model","Unknown"))
            timestamp = str(tags.get("EXIF DateTimeOriginal","Unknown"))
            gps = str(tags.get("GPS GPSLatitude","Unknown"))

            db.insert_metadata((image_path,camera,timestamp,gps))

    except:
        pass