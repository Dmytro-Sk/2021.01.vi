import scrapy
from scrapy.crawler import CrawlerProcess
import re

from vi_news_ycombinator_com.i_news_ycombinator_com.spiders.locators import Locators
from vi_news_ycombinator_com.i_news_ycombinator_com.items import NewsYcombinatorComItem


class NewsYcombinatorComSpider(scrapy.Spider):
    name = 'news_ycombinator_com'
    start_urls = ['']

    custom_settings = {
        # 'FEED_EXPORT_BATCH_ITEM_COUNT': 100,
        'FEED_FORMAT': 'csv',
        'FEED_URI': f"../../iii_results/%(batch_id)02d-{'_'.join(re.findall(r'[A-Z][^A-Z]*', __qualname__)[:-1]).lower()}.csv",
        'FEED_EXPORT_FIELDS': []
    }

    def parse(self, response, **kwargs):
        items = NewsYcombinatorComItem()
        yield items


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(NewsYcombinatorComSpider)
    process.start()
