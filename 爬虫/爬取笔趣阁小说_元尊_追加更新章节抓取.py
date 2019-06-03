# coding=utf-8
# time:2019-06-03

import requests
from pyquery import PyQuery as pq


def user_if_exits():
    global url_list
    url_list = []
    with open(file='url_list.txt', mode='r', encoding='utf-8') as u:
        data = u.readlines()
        for line in data:
            url_list.append(line.strip())


def init():
    global links
    url_start = 'http://www.xbiquge.la/14/14930/'
    response = requests.get(url_start)
    response.encoding = response.apparent_encoding
    doc = pq(response.text)
    links = doc('#list > dl > dd > a')


def get_want():
    for link in links.items():
        url = 'http://www.xbiquge.la' + link.attr.href
        if url in url_list:
            pass
        else:
            with open(file='url_list.txt', mode='a+', encoding='utf-8') as u:
                u.write(url)
                u.write('\n')
            response = requests.get(url)
            response.encoding = response.apparent_encoding
            doc = pq(response.text)
            title = doc('#wrapper > div.content_read > div > div.bookname > h1').text()
            content = doc('#content').text()

            with open(file='元尊.txt', mode='a+', encoding='utf-8') as f:
                f.write(title)
                f.write('\n')
                f.write(content)
                f.write('\n')
            print('%s 抓取完成' % title)


def main():
    user_if_exits()
    init()
    get_want()


main()
