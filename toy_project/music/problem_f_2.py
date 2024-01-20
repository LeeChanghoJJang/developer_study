"""
    장르에 acoustic이 포함된 아티스트 이름 목록 출력하기
"""

import json
from pprint import pprint
import os
os.chdir('./data/artists')
file_names = os.listdir()
sing_names = [os.path.splitext(filename)[0] for filename in file_names]

def acoustic_artists():
    acoustic_json = open('../genres.json',encoding='utf-8')
    acoustics= json.load(acoustic_json)
    for acoustic in acoustics:
        if acoustic['name'] =='acoustic':
            acoustic_id = acoustic['id']
    temp =[]
    for sing_number in sing_names:
        art_json = open(f"{sing_number}.json",encoding="utf-8")
        art= json.load(art_json)
        
        if type(art['genres_ids']) ==int:
            if art['genres_ids'] ==acoustic_id:
                temp.append(art['name'])
        elif type(art['genres_ids']) ==list:
            if acoustic_id in art['genres_ids']:
                temp.append(art['name'])
    return temp


# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    pprint(acoustic_artists())
