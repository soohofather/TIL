import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.  

    a = movie['genre_ids']          # a = [18, 80]
    b = []
    for bb in genres:
        if bb['id'] in a:
            b.append(bb['name'])    # b 에다가 장르 '키값' 중에 a에 있는 것을 추가함. a = [18, 80]에서 b = ['Crime', 'Drama']로 바뀜

    c = {
        'genre_names': b,
        'id': movie['id'],
        'overview': movie['overview'],
        'title': movie['title'],
        'vote_average': movie['vote_average'],
    }
    return c

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))