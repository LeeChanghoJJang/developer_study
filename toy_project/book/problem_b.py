import json
from pprint import pprint

def book_info(book, categories):
    # 여기에 코드를 작성합니다.
    new_dict ={}
    for i in ['id','author','priceSales','description','cover','categoryId']:
        new_dict[i]=book[i]

    temp=[]
    for i in new_dict['categoryId']:    
        for item in categories:
            if i == item['id']:
                temp.append(item['name'])
    new_dict['categoryName'] = temp
    del new_dict['categoryId']
            
    return new_dict

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)
    pprint(book_info(book, categories_list))