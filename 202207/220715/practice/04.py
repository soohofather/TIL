import json
from pprint import pprint


def movie_info(movie):
    pass 
    # 여기에 코드를 작성합니다.    
a = open('./data/movie.json', 'r', encoding='utf-8')
m = json.load(a)

finding = ['id', 'title', 'vote_average', 'overview', 'genre_ids']
dict = {}

for mm in m:
    if mm in finding:
       dict[mm] = dict.get(mm, m[mm])
pprint(dict)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))