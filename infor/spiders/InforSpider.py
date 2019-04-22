import scrapy
import re
from infor.items import InforItem
from scrapy.linkextractors import LinkExtractor
class InforSpider(scrapy.Spider):
    name = 'infor'
    start_urls = ['http://books.toscrape.com/']
    def parse(self, response):
        next_url_book = response.selector.xpath('//div[@class="image_container"]/a/@href')
        for next in next_url_book:
            next_url = response.urljoin(next.extract())
            self.page =re.compile('\d').findall(response.selector.xpath('//li[@class = "next"]/a/@href').extract_first())
            yield scrapy.Request(next_url, callback=self.get_infor)


        next_url_page = response.selector.xpath('//li[@class = "next"]/a/@href').extract_first()
        #http://books.toscrape.com/catalogue/page-2.html
        if next_url_page:
            next_url = response.urljoin(next_url_page)
            yield scrapy.Request(next_url,callback=self.parse)

    def get_infor(self,response):
        item = InforItem()
        item['page'] = self.page
        item['name'] = response.selector.xpath('//div[@class ="col-sm-6 product_main"]/h1/text()').extract_first()
        item['price'] = response.selector.xpath('//div[@class ="col-sm-6 product_main"]/p[@class ="price_color"]/text()').extract_first()
        item['description'] = response.selector.xpath('//div[@id="content_inner"]/article/p/text()').extract_first()
        item['UPC'] = response.selector.xpath('//div[@id="content_inner"]/article/table/tr[1]/td/text()').extract_first()
        item['Availability'] = response.selector.xpath('//div[@id="content_inner"]/article/table/tr[6]/td/text()').extract_first()
        item['Numberofreviews'] = response.selector.xpath('//div[@id="content_inner"]/article/table/tr[7]/td/text()').extract_first()
        yield item








