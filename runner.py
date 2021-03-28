from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from vk.tokyofasion import settings
from vk.tokyofasion.tokyo import TokyoSpider


if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(TokyoSpider, search='токио')

    process.start()