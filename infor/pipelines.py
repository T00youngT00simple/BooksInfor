# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.item import Item

class InforPipeline(object):
    def process_item(self, item, spider):
        return item

class MongoDBPipeline(object):
    DB_URL ='mongodb://localhost:27017'
    DB_NAME = 'scrapy_test'
    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.DB_URL)
        self.db = self.client[self.DB_NAME]

    def close_spider(self,spider):
        self.client.close()

    def process_item(self,item,spider):
        collection = self.db[spider.name]
        post = dict(item) if isinstance(item,Item) else item
        collection.insert_one(post)
        return  item
