import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다. 

    d = []
    for ml in movies:
        a = ml['genre_ids']

        c = []
        for b in genres:
             if b['id'] in a :
                c.append(b['name'])

        e = {
        'genre_names': c,
        'id': ml['id'],
        'overview': ml['overview'],
        'title': ml['title'],
        'vote_average': ml['vote_average'],
            }
        d.append(e)

    return d

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))