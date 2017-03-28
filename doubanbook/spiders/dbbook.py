# -*- coding: utf-8 -*-
import scrapy
import re
from doubanbook.items import DoubanbookItem

class DbbookSpider(scrapy.Spider):
    name = "dbbook"
    #allowed_domains = ["https://www.douban.com/doulist/241262/"]
    start_urls = ['http://www.douban.com/doulist/241262//']

    def parse(self, response):
        #print response.body
        item = DoubanbookItem()
        selector = scrapy.Selector(response)
        albums = selector.xpath('//div[@class="bd doulist-subject"]')
        for each in albums:
            title = each.xpath('div[@class="title"]/a/text()').extract()[0]
            title = title.replace(' ','').replace('\n','')
            rate = each.xpath('div[@class="rating"]/span[@class="rating_nums"]/text()').extract()[0]
            artist = re.search('<div class="abstract">(.*?)<br',each.extract(),re.S).group(1)
            artist = artist.replace(' ','').replace('\n','')
            item['title'] = title
            item['rate'] = rate
            item['artist'] = artist
            #print 'title' + title
            #print 'rate' + rate
            #print artist
            print ''
            yield item