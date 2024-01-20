import json
from pprint import pprint


def books_info(books, categories):
    book_master =[]
    for book in books:
        new_dict={}
        for index in ['author','categoryId','cover','description','id','priceSales','title']:
            if index == 'categoryId':
                temp=[]
                for cate in book['categoryId']:
                    for category in categories:
                        if category['id'] == cate: 
                            temp.append(category['name'])
                new_dict['categoryName'] = temp 
            else:
                new_dict[index] = book[index]
        book_master.append(new_dict)
    return book_master

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))

