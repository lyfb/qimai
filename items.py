# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QimaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = 'qimai_rank'

    rank = scrapy.Field()
    app_id = scrapy.Field()
    app_name = scrapy.Field()
    country = scrapy.Field()
    icon = scrapy.Field()
    price = scrapy.Field()
    publisher = scrapy.Field()
    comment_num = scrapy.Field()
    rating = scrapy.Field()
    company_id = scrapy.Field()
    company_name = scrapy.Field()
    last_releasetime = scrapy.Field()