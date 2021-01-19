# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsYcombinatorComItem(scrapy.Item):
    name = scrapy.Field()
    person_id = scrapy.Field()
    location = scrapy.Field()
    remote = scrapy.Field()
    willing_to_relocate = scrapy.Field()
    technologies = scrapy.Field()
    cv_link = scrapy.Field()
    email = scrapy.Field()
    linkedin = scrapy.Field()
    about = scrapy.Field()
    source = scrapy.Field()
