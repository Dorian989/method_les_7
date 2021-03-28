
import scrapy



class VkItem(scrapy.Item):
    _id = scrapy.Field()
    date = scrapy.Field()
    text = scrapy.Field()
    url = scrapy.Field()
    photos = scrapy.Field()
    title = scrapy.Field()
    likes = scrapy.Field()
    reposts = scrapy.Field()
    view = scrapy.Field()






