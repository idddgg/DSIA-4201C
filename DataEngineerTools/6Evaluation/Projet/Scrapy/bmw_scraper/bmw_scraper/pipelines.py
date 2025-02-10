import pymongo

class MongoDBPipeline:
    """
    Pipeline qui se connecte à MongoDB, transforme les items en JSON (dictionnaires)
    et les insère dans la collection appropriée.
    """
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        mongo_uri = crawler.settings.get('MONGO_URI', 'mongodb://db:27017')
        mongo_db = crawler.settings.get('MONGO_DATABASE', 'bmw_scraping')
        return cls(mongo_uri, mongo_db)

    def open_spider(self, spider):
        spider.logger.info("Connexion à MongoDB : %s", self.mongo_uri)
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()
        spider.logger.info("Connexion MongoDB fermée.")

    def process_item(self, item, spider):
        if spider.name == 'bmw_models':
            transformed_item = {
                'model': item.get('model', None),
                'fuel_type': item.get('fuel_type', None),
                'price': item.get('price', None),
                'image_url': item.get('image_url', None)
            }
            collection = self.db['bmw_models']
        elif spider.name in ['bmw_video', 'bmw_electric_video']:
            transformed_item = {
                'video_url': item.get('video_url', None)
            }
            collection = self.db['bmw_videos']
        else:
            transformed_item = dict(item)
            collection = self.db['scraped_items']

        result = collection.insert_one(transformed_item)
        spider.logger.info("Insertion réussie dans %s avec id : %s", collection.name, result.inserted_id)
        return item
