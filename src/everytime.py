import bs4
import json
import requests

class Everytime():
    def __init__(self):
        self._s = requests.Session()
        self._s.headers.update({
            'Content-Type': 'application/json; charset=utf-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
        })

    def __del__(self):
        self._s.close()

    def _get_request(self, url):
        return self._s.get(url)

    def _post_request(self, url, data={}):
        return self._s.post(url, json.dumps(data))

    def login(self, id, password):
        res = self._post_request('https://everytime.kr/user/login', {
            'userid': id,
            'password': password,
            'redirect': '/'
        })
        return not ('history.go(-1)' in res.text)

    def show_board(self, number, start=0):
        res = self._post_request('https://api.everytime.kr/find/board/article/list', {
            'id': number,
            'moiminfo': 'true',
            'start_num': start,
            'limit_num': '20'
        })
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        return {
            'title': soup.find('moim')['name'],
            'articles': [ int(x['id']) for x in soup.find_all('article') ]
        }

    def show_article(self, number):
        res = self._post_request('https://api.everytime.kr/find/board/comment/list', {
            'id': number,
            'limit_num': -1
        })
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        return {
            'title': soup.find('article')['title'],
            'content': soup.find('article')['text']
        }
