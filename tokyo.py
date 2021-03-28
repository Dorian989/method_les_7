import time
import scrapy
from items import VkItem
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
import response
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
actionChains = ActionChains(driver)



DRIVER_PATH = "./chromedriver"


class TokyoSpider(scrapy.Spider):
    name = 'tokyo'
    allowed_domains = ['vk.com']
    start_urls = ['http://vk.com/tokyofashion']

    def __init__(self, search):
        self.start_urls = [f'https://vk.com/tokyofashion']


    def scroll(self):
        url = 'https://vk.com/tokyofashion'
        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(url)
        post_links = 'https://vk.com/tokyofashion?w=wall-' + response.xpath('//div[@class="wide_column"]//div[@class="wall_module"]//div[@class="wall_posts own mark_top "]/div[contains(@id, "post-")]')
        for link in post_links:
            yield response.follow(link, callback=self.handle_post_data)
        yield response.follow(callback=self.parse)


        for i in range(5):
            time.sleep(5)
            article = driver.find_elements_by_tag_name("article")[-1]
            actions = ActionChains(driver)
            actions.move_to_element(article)
            actions.perform()

    def find(self):
     url = 'https://vk.com/tokyofashion'
     find = driver.find_elements_by_tag_name('ui_tab_plain ui_tab_search')
     find.actionChains.context_click('/wall-29341229?search=1').perform()
     driver.get(url)
     tape = driver.find_element_by_name("ui_search_field _field")
     tape.send_keys("токио")


    def handle_post_data(self, response: HtmlResponse):
        loader = ItemLoader(item=VkItem(), response=response)
        loader.add_value('date', '//div/a/span[@class="rel_date"]')
        loader.add_value('text', '//div/div[@class="wall_post_text"]/text()')
        loader.add_value('url', response.url)
        loader.add_xpath('photos', '//div//div//div/img[@src]')
        loader.add_xpath('likes','message_count', 'reposts', '//div[@class="_post_content"]/div[@class="post_content"]/div[@class="post_info"]/div/div/div/a/div[@class="like_button_count"]')
        loader.add_xpath('view', '//div/div/div[@class="like_views _views"]')
        yield loader.load_item()