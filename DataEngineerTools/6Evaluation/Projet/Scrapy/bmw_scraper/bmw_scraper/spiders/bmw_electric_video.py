import scrapy
from bmw_scraper.items import BmwVideoItem

class BmwElectricVideoSpider(scrapy.Spider):
    name = 'bmw_electric_video'
    # On change ici le domaine pour pointer vers bmwgroup.com
    allowed_domains = ['bmwgroup.com']
    start_urls = ['https://www.bmwgroup.com/en.html']

    def parse(self, response):
        self.logger.info("Parsing logos on : %s", response.url)
        # Sélection de toutes les images du header
        images = response.xpath("//img[@class='grp-header__logo']")
        if not images:
            self.logger.warning("Aucune image trouvée sur %s", response.url)

        for img in images:
            src = img.xpath("./@src").get()
            if src:
                # Création d'un item identique à celui que tu utilisais pour la vidéo
                item = BmwVideoItem()
                # On stocke l'URL dans video_url pour ne pas casser le pipeline existant
                item['video_url'] = response.urljoin(src)
                yield item
