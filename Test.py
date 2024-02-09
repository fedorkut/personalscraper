import scrapy
from quotes_js_scraper.items import QuoteItem
from selenium.webdriver.firefox.service import Service as FirefoxService
from scrapy_selenium import SeleniumRequest
from shutil import which


class QuotesSpider(scrapy.Spider):
    name = 'links'
    
    def start_requests(self):
        url = 'https://www.twitch.tv/quin69/about'
        yield SeleniumRequest(url=url, callback=self.parse, wait_time=20) 

    def parse(self, response):
        for link in response.css('a::attr(href)').getall()
        for link in links: 
            quote_item = QuoteItem ()
            quote_item ['url'] = response.urljoin(link)
            yield quote_item
