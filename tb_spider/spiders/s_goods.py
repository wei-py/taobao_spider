import scrapy, re
from tb_spider.items import TbSpiderItem


class SGoodsSpider(scrapy.Spider):
    name = 's_goods'
    goods = '茶'
    allowed_domains = []
    start_urls = [f'https://s.taobao.com/search?q=茶&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20210405&ie=utf8&bcoffset=4&p4ppushleft=1%2C48&s={44 * i}' for i in range(50)]


    def parse(self, response):
        print(response.url)
        goods = re.findall('i2iTags(.*?)"risk', response.text)
        item = TbSpiderItem()
        with open('taobao.html', 'w') as f:
            f.write(response.text)
        # raw_title view_fee  item_loc  view_sales  comment_count nick  view_price  detail_url
        for good in goods:
            try:
                raw_title = self.match_str('raw_title', good)
                view_fee = self.match_str('view_fee', good)
                item_loc = self.match_str('item_loc', good)
                view_sales = self.match_str('view_sales', good)
                comment_count = self.match_str('comment_count', good)
                nick = self.match_str('nick', good)
                view_price = self.match_str('view_price', good)
                detail_url = self.match_str('detail_url', good)
            except IndexError:
                print(raw_title, view_fee,item_loc,view_sales, comment_count, nick, view_price, detail_url)
            item['raw_title'] = raw_title
            item['view_fee'] = view_fee
            item['item_loc'] = item_loc
            item['view_sales'] = view_sales
            item['comment_count'] = comment_count
            item['nick'] = nick
            item['view_price'] = view_price
            item['detail_url'] = detail_url
            print(item)
            yield item

    def match_str(self, attribute, good):
        attribute = re.findall(f'{attribute}":"(.*?)","', good)
        if len(attribute) > 0:
            return attribute[0]
        else:
            return ''



            
        