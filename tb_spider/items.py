# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TbSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # raw_title view_fee  item_loc  view_sales  comment_count nick  view_price  detail_url
    raw_title = scrapy.Field()
    view_fee = scrapy.Field()
    item_loc = scrapy.Field()
    view_sales = scrapy.Field()
    comment_count = scrapy.Field()
    nick = scrapy.Field()
    view_price = scrapy.Field()
    detail_url = scrapy.Field()

    
