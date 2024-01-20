"""
    팔로워가 5,000,000이상, 10,000,000미만인 아티스트들을 
    아티스트 이름과 팔로워를 목록으로 출력하기
"""

import json
from pprint import pprint
import os
os.chdir('./data/artists')
file_names = os.listdir()
sing_names = [os.path.splitext(filename)[0] for filename in file_names]
def get_popular():
    popular_artist=[]
    for sing_number in sing_names:
        art_json = open(f"{sing_number}.json",encoding="utf-8")
        art= json.load(art_json)
        if 5000000<= art['followers']['total'] < 10000000:
            popular_artist.append({'followers':art['followers']['total'],
                                   'name':art['name']})
    return popular_artist


# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    pprint(get_popular())
