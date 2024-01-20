import json

def max_polularity(artists):
    max_popular=0
    for artist in artists:
        art_json = open(f"data/artists/{artist['id']}.json",encoding="utf-8")
        art= json.load(art_json)
        if art['popularity'] > max_popular:
            max_popular = art['popularity']
            best_artist= art['name']
    return best_artist

# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    artists_json = open("data/artists.json", encoding="utf-8")
    artists_list = json.load(artists_json)

    print(max_polularity(artists_list))
