from pymongo import MongoClient

# Connexion à MongoDB via Docker (service "db" dans docker-compose.yml)
MONGO_URI = "mongodb://db:27017/"
DATABASE_NAME = "bmw_scraping"

# Connexion unique
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

def get_db():
    """Retourne l'objet base de données MongoDB."""
    return db

def get_video_url():
    """Récupère la première vidéo valide depuis la collection `bmw_videos`."""
    db = get_db()
    video = db.bmw_videos.find_one({"video_url": {"$regex": "\\.mp4$"}}, {"_id": 0, "video_url": 1})
    return video["video_url"] if video else None  # Retourne l'URL ou None si aucune vidéo valide

def get_logo_urls():
    """Récupère les URLs des logos depuis la collection `bmw_videos`, en excluant les vidéos."""
    db = get_db()
    logos = db.bmw_videos.find(
        {"video_url": {"$not": {"$regex": r"\.mp4$"}}},  # Exclut les fichiers .mp4
        {"_id": 0, "video_url": 1}
    )
    logo_urls = [logo["video_url"] for logo in logos]
    return logo_urls

def get_specific_image():
    """Récupère l'URL de l'image spécifique depuis la collection `scraped_items`."""
    db = get_db()
    image = db.scraped_items.find_one({}, {"_id": 0, "video_url": 1})  # Récupère la première entrée
    return image["video_url"] if image else None  # Retourne l'URL ou None si vide

def get_all_cars():
    """Récupère toutes les voitures BMW stockées en base en filtrant les entrées invalides."""
    db = get_db()
    cars = list(db.bmw_models.find({}, {"_id": 0}))
    return [car for car in cars if "fuel_type" in car and car["fuel_type"]]  # Filtrer les entrées invalides
