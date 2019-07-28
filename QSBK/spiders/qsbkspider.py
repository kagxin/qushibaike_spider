# -*- coding: utf-8 -*-
import scrapy
from QSBK.items import ArticleItemLoader, QsbkItem


class QsbkspiderSpider(scrapy.Spider):
    name = 'qsbkspider'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/hot/']

    def parse(self, response):
        for res in response.xpath('//div[@id="content-left"]/div'):
            item_loader = ArticleItemLoader(item=QsbkItem(), selector=res)
            item_loader.add_xpath('age', 'div[1]/div[1]/text()')
            item_loader.add_xpath('sex', 'div[1]/div[1]/@class')
            item_loader.add_xpath('user_name', 'div[1]/a[2]/h2/text()')
            item_loader.add_xpath('content', 'a[1]/div/span/text()')
            item_loader.add_xpath('funny_num', 'div[2]/span[1]/i/text()')
            item_loader.add_xpath('comment_num', 'div[2]/span[2]/a/i/text()')

            yield item_loader.load_item()
        next_page_url = response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').get()
        if next_page_url:
            yield response.follow(next_page_url, self.parse)
