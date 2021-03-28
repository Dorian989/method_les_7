from itemadapter import ItemAdapter
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from pymongo import MongoClient


class TokyofasionPipeline:
    def process_item(self, item, spider):
        return item
class DataBasePipeline(object):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.vk_photo

    def process_item(self, item, spider):
        collection = self.mongo_base[spider.name]
        collection.update_one(item)
        return item

class VkPhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photos']:
            for img in item['photos']:
                try:
                    yield scrapy.Request(img, meta=item)
                except Exception as e:
                    print(e)

    def file_path(self, request, response=None, info=None, ):
        item_title = request.meta['title']
        return f'{item_title}/{ImagesPipeline.file_path(self, request, response, info)}'

    def item_completed(self, results, item, info):
        if results:
            item['photos'] = [itm[1] for itm in results if itm[0]]
            return item