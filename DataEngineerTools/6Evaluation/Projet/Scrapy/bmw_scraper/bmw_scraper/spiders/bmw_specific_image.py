import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from scrapy.selector import Selector
from time import sleep
from bmw_scraper.items import BmwVideoItem

class BmwSpecificImageSpider(scrapy.Spider):
    name = 'bmw_specific_image'
    start_urls = ['https://www.bmwgroup.com/en.html']

    def __init__(self, *args, **kwargs):
        super(BmwSpecificImageSpider, self).__init__(*args, **kwargs)
        
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Exécuter Chrome sans interface
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Utilisation du ChromeDriver installé dans Docker
        service = Service("/usr/local/bin/chromedriver")
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        self.logger.info("Chargement de la page avec Selenium...")

        # Charger la page dans Selenium
        self.driver.get(response.url)
        sleep(5)  # Temps d'attente pour que le JavaScript charge l'image

        # Récupération du HTML après chargement
        html = self.driver.page_source
        sel = Selector(text=html)

        # Sélectionner l'image spécifique "Header_History_iDrive"
        specific_image = sel.xpath("//img[contains(@src, 'Header_History_iDrive')]/@src").get()
        self.logger.info(f"Image trouvée : {specific_image}")

        if specific_image:
            item = BmwVideoItem()
            item['video_url'] = response.urljoin(specific_image)  # URL absolue
            yield item
        else:
            self.logger.warning("❌ Aucune image spécifique trouvée ! Vérifie le XPath ou la page.")

        # Fermer le driver Selenium
        self.driver.quit()
