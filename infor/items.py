# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class InforItem(scrapy.Item):
    # define the fields for your item here like:
    page =scrapy.Field()
    name = scrapy.Field()
    price =scrapy.Field()
    description = scrapy.Field()
    UPC =scrapy.Field()
    Availability =scrapy.Field()
    Numberofreviews = scrapy.Field()

    pass
