import json
from pprint import pprint
def dec_artists(artists):
    temp=[]
    for artist in artists:
        art_json = open(f"data/artists/{artist['id']}.json",encoding="utf-8")
        art= json.load(art_json)
        if art['followers']['total'] >=10000000:
            temp.append({'name': art['name'],'uri-id' : art['uri'][15:]})
    return temp

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    pprint(dec_artists(artists_list))
