import time
import requests
from requests_html import HTMLSession

# session = HTMLSession()
# login_url = 'https://login.taobao.com/member/login.jhtml'
# url  = 'https://s.taobao.com/search?q=优衣库&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=2&p4ppushleft=1%2C48&ntoffset=2&s=132'
# with open('/Users/wei/python3_venv/tb_spider/tb_spider/spiders/cookies.txt', 'r') as f:
#     cookies = f.read()
# cookies = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookies.split('; ')}
#
# resp = session.get(url, cookies=cookies)
#
#
#
# time.sleep(3)
# print(resp.text)
# print(resp.url)
# with open('taobao.html', 'w') as f:
#     f.write(resp.text)

goods = '茶'
page = 0
start_urls = [f'https://s.taobao.com/search?q={goods}&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20210405&ie=utf8&bcoffset=4&p4ppushleft=1%2C48&s={44 * i}' for i in range(100)]
for url in start_urls:
    print(type(url))