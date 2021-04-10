# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from openpyxl import Workbook
import pymysql as pq

class TbSpiderPipeline:
    # def __init__(self):
    #     self.conn = pq.connect(host='localhost', user='root',
    #                            passwd='', db='spiders', charset='utf8')
    #     self.cur = self.conn.cursor()

    # # raw_title view_fee  item_loc  view_sales  comment_count nick  view_price  detail_url
    # def process_item(self, item, spider):
    #     raw_title = item.get("raw_title")  # 有的图书有数据项缺失，这里做了容错处理
    #     view_fee = item.get("view_fee")
    #     item_loc = item.get("item_loc")
    #     view_sales = item.get("view_sales")
    #     comment_count = item.get("comment_count")
    #     nick = item.get("nick")
    #     view_price = item.get("view_price")
    #     detail_url = item.get("detail_url")

    #     sql = "insert into tb_spider(raw_title, view_fee, item_loc, view_sales, comment_count, nick, view_price, detail_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    #     self.cur.execute(sql, (raw_title, view_fee, item_loc, view_sales, comment_count, nick, view_price, detail_url))
    #     self.conn.commit()

    # def close_spider(self, spider):
    #     self.cur.close()
    #     self.conn.close()

    # def process_item(self, item, spider):
    #     print(item)
    #     return item
    

    # # raw_title view_fee  item_loc  view_sales  comment_count nick  view_price  detail_url
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['raw_title', 'view_fee', 'item_loc', 'view_sales', 'comment_count', 'nick', 'view_price', 'detail_url'])

    def process_item(self, item, spider):
        line = [item['raw_title'], item['view_fee'], item['item_loc'], item['view_sales'], item['comment_count'], item['nick'], item['view_price'], item['detail_url']]
        self.ws.append(line)
        self.wb.save('tb_goods.xlsx')
        return item
