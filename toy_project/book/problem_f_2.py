import json
import os 

def sorted_cs_books_by_price(books, categories):
    # 컴퓨터 공학 categoryID 추출
    for category in categories:
        if category['name'] == '컴퓨터 공학':
            category_id = category['id']

    price_books = dict()
    for book in books: # 모든 북파일 열기
        book_json= open(f'data/books/{book["id"]}.json',encoding='utf-8')
        book_file = json.load(book_json)
        # book_file의 categoryID를 컴퓨터공학과 비교
        if type(book_file['categoryId']) == list:
            if category_id in book_file['categoryId']:
                price_books.update({book_file['title']:book_file['priceSales']})
        elif type(book_file['categoryId']) ==int:
            if category_id == book_file['categoryId']:
                price_books.update({book_file['title']:book_file['priceSales']})
        sorted(list(price_books),key = lambda x : x[1])
    return price_books
            
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    print(sorted_cs_books_by_price(books, categories_list))
