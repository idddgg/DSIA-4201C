import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from scrapy.selector import Selector
from time import sleep

class BmwModelsSpider(scrapy.Spider):
    name = 'bmw_models'
    start_urls = ['https://www.bmw.fr/fr/tous-les-modeles.html']

    def __init__(self, *args, **kwargs):
        super(BmwModelsSpider, self).__init__(*args, **kwargs)
        
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        # Utilisation du ChromeDriver installé dans le Dockerfile
        service = Service("/usr/local/bin/chromedriver")
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        self.driver.get(response.url)
        sleep(10)  # Ajustez le délai si nécessaire
        
        html = self.driver.page_source
        sel = Selector(text=html)
        
        cars = sel.css('div.cmp-modelcard')
        for car in cars:
            model = car.css('button[data-cmp-hook-modelselection="button"]::attr(title)').get()
            fuel_type = car.css('div.cmp-modelcard__fuel-type span::text').get()
            price = car.css('span.cmp-modelcard__price::text').get()
            image_url = car.css('img.cmp-cosy-img.cmp-modelcard__cosy-img::attr(src)').get()
            if not image_url:
                image_url = car.css('img.cmp-cosy-img::attr(data-src)').get() or \
                            car.css('img.cmp-cosy-img::attr(srcset)').get()
                            
            yield {
                'model': model.strip() if model else None,
                'fuel_type': fuel_type.strip() if fuel_type else None,
                'price': price.strip() if price else None,
                'image_url': response.urljoin(image_url) if image_url else None,
            }
        self.driver.quit()
