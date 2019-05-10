# -*- coding: utf-8 -*-
import scrapy
from scrapy_spider.items import QuoteItem

class QuotesSpiderSpider(scrapy.Spider):
    name = 'quotes_spider'
    allowed_domains = ['megamart.az']
    start_urls = ['https://www.megamart.az/az/by-category/5792-metbex-ucun']

    def parse(self, response):
        SET_SELECTOR='//div[@class="filters-grid all-filters col-lg-15 col-md-20 col-sm-20 col-xs-60"]'
        next_page_url = response.xpath("//div[@class='product-img with-image']//a/@href").extract_first()
        for i in response.xpath(SET_SELECTOR):
            yield {
                'title':i.xpath('.//div/h5/a/text()').extract_first(),
                'price':i.xpath('.//div/span/text()').extract_first(),
                #'img':i.xpath('.//div/a/img/text()').extract_first(),

            } 

            

        next_page_url = response.xpath("//li[@class='next']//a/@href").extract_first()
        if next_page_url:
            absolute_next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(absolute_next_page_url)