# coding=utf-8
# time:2019-06-03


import requests
from pyquery import PyQuery as pq

# 进入排行榜，获取排行榜的小说链接，总、月、周、日榜的小说链接地址去重，得到difference_link
url = 'http://www.xbiquge.la/paihangbang/'
response = requests.get(url)
response.encoding = response.apparent_encoding
doc = pq(response.text)
links = doc('#main > div:nth-child(2)>ul>li>a')
difference_link = set()
for link in links.items():
    difference_link.add(link.attr.href)

# 得到了排行榜的小说，逐个获取小说的内容
for link in difference_link:
    response = requests.get(link)
    response.encoding = response.apparent_encoding
    doc = pq(response.text)
    links = doc('#list > dl >dd >a')  # 排行榜对应小说页面，获取所有的章节链接
    name = doc('#info > h1').text()
    with open(file=name + '.txt', mode='a+', encoding='utf-8') as f:

        # 获取所有的章节链接的内容
        for link1 in links.items():
            url = 'http://www.xbiquge.la/' + link1.attr.href
            response = requests.get(url)
            response.encoding = response.apparent_encoding
            doc1 = pq(response.text)
            title = doc1('#wrapper > div.content_read > div > div.bookname > h1').text()
            content = doc1('#content').text()
            print('正在爬取 %s %s' % (name, title))

            f.write(title)
            f.write('\n')
            f.write(content)
            f.write('\n')
