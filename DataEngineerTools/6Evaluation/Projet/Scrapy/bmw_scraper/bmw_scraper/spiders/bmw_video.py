import scrapy
from bmw_scraper.items import BmwVideoItem

class BmwVideoSpider(scrapy.Spider):
    name = 'bmw_video'
    start_urls = ['https://www.bmwgroup.jobs/fr/fr.html']

    def parse(self, response):
        self.logger.info("Parsing page vidéo : %s", response.url)
        video_url = response.css('video source::attr(src)').get()
        if video_url:
            absolute_video_url = response.urljoin(video_url)
            item = BmwVideoItem()
            item['video_url'] = absolute_video_url
            yield item
        else:
            self.logger.warning("Aucune vidéo trouvée sur %s", response.url)
