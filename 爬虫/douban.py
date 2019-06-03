# coding=utf-8


import requests
from bs4 import BeautifulSoup
import json

def get_url():
    url = 'https://movie.douban.com/cinema/nowplaying/dongguan/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    }
    response = requests.get(url,headers=headers)
    return response.text


def parase_response(text):
    soup = BeautifulSoup(text, 'lxml')
    LiList = soup.find_all('li', attrs={"data-category":"nowplaying"})
    movies = []
    for li in LiList:
        movie = {}
        title = li['data-title']
        score = li['data-score']
        star = li['data-star']
        release = li['data-release']
        region = li['data-region']
        actors = li['data-actors']

        movie['title'] = title
        movie['score'] = score
        movie['star'] = star
        movie['release'] = release
        movie['region'] = region
        movie['actors'] = actors

        movies.append(movie)
    return movies


def save_data(data):
    with open(file='douban.json', mode='w', encoding='utf-8') as f:
        json.dump(movies, f, ensure_ascii=False)


if __name__ == '__main__':
    text = get_url()
    movies = parase_response(text)
    for movie in movies:
        print(movie)
