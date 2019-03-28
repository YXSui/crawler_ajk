# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AjkItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    structure = scrapy.Field()
    area = scrapy.Field()
    rise = scrapy.Field()
    year = scrapy.Field()
    price = scrapy.Field()
    unit_price = scrapy.Field()
    address = scrapy.Field()
    owner = scrapy.Field()
    pass
