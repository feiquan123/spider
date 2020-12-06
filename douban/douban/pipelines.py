# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from douban.settings import mongo_url,mongo_collection,mongo_db


class DoubanPipeline:
    def __init__(self):
        dbname = mongo_db
        sheetname = mongo_collection
        client = pymongo.MongoClient(mongo_url)
        mydb = client[dbname]
        self.post = mydb[sheetname]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
