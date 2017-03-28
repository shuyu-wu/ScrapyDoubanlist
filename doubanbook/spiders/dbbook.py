# -*- coding: utf-8 -*-
import scrapy
import re


class DbbookSpider(scrapy.Spider):
    name = "dbbook"
    #allowed_domains = ["https://www.douban.com/doulist/241262/"]
    start_urls = ['http://www.douban.com/doulist/241262//']

    def parse(self, response):
        #print response.body
        selector = scrapy.Selector(response)
        albums = selector.xpath('//div[@class="bd doulist-subject"]')
        for each in albums:
            title = each.xpath('div[@class="title"]/a/text()').extract()[0]
            rate = each.xpath('div[@class="rating"]/span[@class="rating_nums"]/text()').extract()[0]
            artist = re.search('<div class="abstract">(.*?)<br',each.extract(),re.S).group(1)
            print 'title' + title
            print 'rate' + rate
            print artist
            print ''