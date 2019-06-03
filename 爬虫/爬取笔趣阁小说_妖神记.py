# coding=utf-8
# time:2019-06-03

import requests
from pyquery import PyQuery as pq

url_start = 'http://www.xbiquge.la/2/2699/'
response = requests.get(url_start)
response.encoding = response.apparent_encoding
doc = pq(response.text)
links = doc('#list > dl > dd > a')
for link in links.items():
    url = 'http://www.xbiquge.la' + link.attr.href
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    doc = pq(response.text)
    title = doc('#wrapper > div.content_read > div > div.bookname > h1').text()
    content = doc('#content').text()

    with open(file='妖神记.txt', mode='a+', encoding='utf-8') as f:
        f.write(title)
        f.write('\n')
        f.write(content)
        f.write('\n')
    print('%s 抓取完成' % title)
