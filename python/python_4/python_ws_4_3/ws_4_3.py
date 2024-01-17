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
for i in dummy_data:
    print(i)