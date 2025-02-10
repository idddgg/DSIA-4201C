# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class BmwScraperItem(scrapy.Item):
    # Pour le spider bmw_models
    model = scrapy.Field()
    fuel_type = scrapy.Field()
    price = scrapy.Field()
    image_urls = scrapy.Field()  # Liste d'URLs pour les images

class BmwVideoItem(scrapy.Item):
    # Pour les spiders bmw_video et bmw_electric_video
    video_url = scrapy.Field()   # URL de la vidéo
    file_urls = scrapy.Field()   # Liste d'URLs (si nécessaire)

