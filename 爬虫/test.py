# coding=utf-8
# time:2019-06-03


import requests
from pyquery import PyQuery as pq

url = 'http://www.xbiquge.la/paihangbang/'
response = requests.get(url)
response.encoding = response.apparent_encoding
doc = pq(response.text)
links = doc('#main > div:nth-child(2)>ul>li>a')
difference_link = set()
for link in links.items():
    difference_link.add(link.attr.href)

for link in difference_link:
    response1 = requests.get(link)
    response1.encoding = response1.apparent_encoding
    doc1 = pq(response1.text)
    links1 = doc1('#list > dl >dd >a')

    for link1 in links1.items():
        url1 = 'http://www.xbiquge.la/' + link1.attr.href
        response1 = requests.get(link)
        response1.encoding = response1.apparent_encoding
        doc1 = pq(response1.text)
        title = doc1('#wrapper > div.content_read > div > div.bookname > h1').text()
        content = doc1('#content').text()
        name = doc1('#info > h1').text()
        print(name, url1, title)

        with open(file=name+'.txt', mode='a+', encoding='utf-8') as f:
            f.write(title)
            f.write('\n')
            f.write(content)
            f.write('\n')