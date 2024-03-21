import json
from pprint import pprint


def book_info(book):
    # new_dict ={}
    # for i in ['author','categoryId','cover','description','id','priceSales','title']:
    #     new_dict[i]=book[i]
    new_dict = {i : book[i] for i in ['author','categoryId','cover','description','id','priceSales','title']}
    return new_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    pprint(book_info(book))
