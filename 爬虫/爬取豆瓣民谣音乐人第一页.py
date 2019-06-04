# coding=utf-8
# time:2019/6/4

import requests
from pyquery import PyQuery as pq
import json


for i in range(1,101):
    url = 'https://music.douban.com/artists/genre_page/4/' + str(i)
    response = requests.get(url)
    doc = pq(response.text)
    contents = doc("#content > div > div.article > div:nth-child(2) > div > div  > div > a > img")  # 得到img标签的内容
    print('start get the %d pages' % i)

    for content in contents.items():
        name_pic_dic = {}
        name = content.attr.alt  # img标签里面包含有alt=XXXX，src=xxxx，利用attr属性方法获取对应的指
        src = content.attr.src
        name_pic_dic[name] = src
        # dumps是将dict转化成str格式，loads是将str转化成dict格式,ensure_ascii=False的意思是允许json格式写入其他字符，否则的话不会显示中文
        name_pic_dic = json.dumps(name_pic_dic, ensure_ascii=False)

        with open(file='民谣音乐人前100页.txt', mode='a+', encoding='utf-8') as f:
            f.write(name_pic_dic)
            f.write('\n')
