import requests
API_URL = 'https://jsonplaceholder.typicode.com/users'

response = requests.get(API_URL)
parsed_data = response.json()

dummy_data=[]
for i in range(10):
    if float(parsed_data[i]['address']['geo']['lat']) < 80 and float(parsed_data[i]['address']['geo']['lng']) > (-80):
        temp_dict= {"company":parsed_data[i]['company']['name'],
                    "lat":parsed_data[i]['address']['geo']['lat'],
                    "lng":parsed_data[i]['address']['geo']['lng'],
                     "name": parsed_data[i]['name']}
        dummy_data.append(temp_dict)
# for i in dummy_data:
#     print(i)

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

def create_user(data):
    censored_user_list=dict()

    def censorship(company,name):
        if company not in black_list:
            print('이상 없습니다.')
            return True
        else:
            print(f'{company} 소속의 {name} 은/는 등록할 수 없습니다.')
            return False
        
    for i in range(len(data)):
        company = data[i]["company"]
        name = data[i]["name"]
        if censorship(company,name):
            censored_user_list[company] = [name]
    return censored_user_list

print(create_user(dummy_data))