import json
import os 
# 첫번쨰 방법
'''
os.chdir('./data/books')
file_names = os.listdir()
book_numbers = [os.path.splitext(filename)[0] for filename in file_names]
os.chdir('../')
os.chdir('../')

def best_new_books(book_numbers):
    max_review_book=''
    max_review=0
    for number in book_numbers:
        books_json = open(f'data/books/{number}.json', encoding='utf-8')
        book= json.load(books_json)
        if book['pubDate'][:4]=='2023':
            if book['customerReviewRank']>=max_review:
                max_review = book['customerReviewRank']
                max_review_book = book['title']
    return max_review_book            
'''

def best_new_books(books_list):
    max_review=0
    for book in books_list:
        book_json= open(f'data/books/{book["id"]}.json',encoding='utf-8')
        book_file = json.load(book_json)
        if book_file["pubDate"][:4] == '2023':
            if book_file['customerReviewRank']>=max_review:
                max_review = book_file['customerReviewRank']
                max_review_book = book_file['title']
    return max_review_book

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(best_new_books(books_list))
