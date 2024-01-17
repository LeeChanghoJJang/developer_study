number_of_book = 100
name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]

def create_user(name,age):
    user_info = dict()
    user_info['name'] = name
    user_info['age'] = age
    print(f'{name}님 환영합니다')
    return user_info 

def rental_book(info):
    print(f'남은 책의 수 : {decrease_book(info["age"])}')
    return f'{info["name"]}님이 {age//10}권의 책을 대여하였습니다.'

def decrease_book(age):
    global number_of_book
    number_of_book -= age//10
    return number_of_book

many_user = list(map(create_user,name,age))
info = dict(map(lambda x :(x['name'],x['age']),many_user))

for name,age in info.items():
    rental_info = {'name':name,'age':age}
    print(rental_book(rental_info))
# for i in many_user:
#     print(rental_book(**i))