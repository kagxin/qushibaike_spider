# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class QsbkPipeline(object):

    def __init__(self, client, collection):
        self.collection = collection
        self.client = client

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item

    @classmethod
    def from_settings(cls, settings):
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        mydb = client['qushibaike']
        return cls(client, mydb['artile'])

    def spider_closed(self, spider):
        self.client.close()