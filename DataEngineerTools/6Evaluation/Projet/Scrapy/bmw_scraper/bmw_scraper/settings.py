BOT_NAME = 'bmw_scraper'

SPIDER_MODULES = ['bmw_scraper.spiders']
NEWSPIDER_MODULE = 'bmw_scraper.spiders'

# Ne pas respecter le fichier robots.txt (à ajuster si besoin)
ROBOTSTXT_OBEY = False

# Paramètres de téléchargement
CONCURRENT_REQUESTS = 16
DOWNLOAD_DELAY = 1
COOKIES_ENABLED = False

# Activer notre pipeline MongoDB
ITEM_PIPELINES = {
    'bmw_scraper.pipelines.MongoDBPipeline': 300,
}

# Chemins pour le stockage (non utilisés ici puisque l'insertion est directe dans MongoDB)
IMAGES_STORE = '/app/Data/Images'
FILES_STORE = '/app/Data/Videos'
MEDIA_ALLOW_REDIRECTS = True

# Paramètres de connexion à MongoDB
MONGO_URI = 'mongodb://db:27017'
MONGO_DATABASE = 'bmw_scraping'
