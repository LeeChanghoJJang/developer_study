import json
from pprint import pprint

def artist_info(artist, genres):
    temp=[]
    for art_id in artist['genres_ids']:
        for gen in genres:
            if gen['id'] ==art_id:
                temp.append(gen['name'])
    artist['genres_names'] = temp
    del artist['uri']
    del artist['external_urls']
    del artist['genres_ids']
    return artist


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artist_json = open('data/artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)
    
    # print(artist_dict)
    pprint(artist_info(artist_dict, genres_list))
