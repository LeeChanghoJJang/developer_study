import json
from pprint import pprint
import os 
# 첫번째 방법
'''
os.chdir('./data/books')
file_names = os.listdir()
book_numbers = [os.path.splitext(filename)[0] for filename in file_names]
os.chdir('../')
os.chdir('../')
def best_book():
    max_review = 0
    book_name =''
    for number in book_numbers:
        book_json = open(f'data/books/{number}.json', encoding='utf-8')
        book = json.load(book_json)
        if book['customerReviewRank'] > max_review:
            max_review = book['customerReviewRank']
            book_name = book['title']
    return book_name
'''
# 두번째 방법
def best_book(books_list):
    max_review=0
    for book in books_list:
        book_json= open(f'data/books/{book["id"]}.json',encoding='utf-8')
        book_file = json.load(book_json)
        if book_file['customerReviewRank'] >= max_review:
            max_review = book_file['customerReviewRank']
            book_name = book_file['title']
    return book_name ##why '멋진 신세계'로 출력되는건지?

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    pprint(best_book(books_list))
