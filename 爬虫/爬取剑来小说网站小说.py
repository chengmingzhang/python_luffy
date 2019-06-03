# coding=utf-8
# time:2019-06-03


import requests
from pyquery import PyQuery as pq

def init():
    global url_start
    global links
    url_start = 'http://www.jianlaixiaoshuo.com/'
    response = requests.get(url_start)
    response.encoding = response.apparent_encoding
    doc = pq(response.text)
    links = doc('body > div:nth-child(2) > div > dl > dd > a')  # 获取页面所有的链接


def get_text():
    for link in links.items():
        url = url_start + link.attr.href
        print(url)
        response = requests.get(url)
        response.encoding = response.apparent_encoding
        doc = pq(response.text)
        title = doc('#BookCon > h1').text()
        content = doc('#BookText').text()
        # yield (title+content)  # 测试抓去内容是否准确

        with open(file='雪中悍刀行.txt', mode='a+', encoding='utf-8') as f:
            f.write(title)
            f.write('\n')
            f.write(content)
            f.write('\n')

init()
get_text()