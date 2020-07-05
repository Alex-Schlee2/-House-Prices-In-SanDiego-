# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
# TakeFirst Class, so we dont get back a list as result
from scrapy.loader.processors import TakeFirst


class Zillow2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # TakeFirst Class, so we dont get back a list as result
    addressCity = scrapy.Field(output_processor=TakeFirst())
    addressState = scrapy.Field(output_processor=TakeFirst())
    latitude = scrapy.Field(output_processor=TakeFirst())
    longitude = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(output_processor=TakeFirst())
    area = scrapy.Field(output_processor=TakeFirst())
    baths = scrapy.Field(output_processor=TakeFirst())
    beds = scrapy.Field(output_processor=TakeFirst())
