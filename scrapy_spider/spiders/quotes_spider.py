# -*- coding: utf-8 -*-
import scrapy
from scrapy_spider.items import QuoteItem

class QuotesSpiderSpider(scrapy.Spider):
    name = 'quotes_spider'
    allowed_domains = ['myip.ms']
    start_urls = ['https://myip.ms/browse/ip_addresses/1#top']

    def parse(self, response):
        SET_SELECTOR='//t[@body]'
        #next_page_url = response.xpath("//div[@class='product-img with-image']//a/@href").extract_first()
        for i in response.xpath(SET_SELECTOR):
            yield {
                'title':i.xpath('.//td/span/text()').extract_first(),
                #'price':i.xpath('.//div/span/text()').extract_first(),
                #'img':i.xpath('.//div/a/img/text()').extract_first(),

            } 

            

        next_page_url = response.xpath("//li[@class='next']//a/@href").extract_first()
        if next_page_url:
            absolute_next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(absolute_next_page_url)