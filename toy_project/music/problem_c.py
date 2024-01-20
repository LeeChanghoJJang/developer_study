import json
from pprint import pprint

def artist_info(artists, genres):
    temp=[]
    total_result=[]
    for artist in artists:
        for art_id in artist['genres_ids']:
            for gen in genres:
                if gen['id'] ==art_id:
                    temp.append(gen['name'])
        artist['genres_names'] = temp
        del artist['uri']
        del artist['external_urls']
        del artist['genres_ids']
        total_result.append(artist)
    return total_result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artists_list, genres_list))
