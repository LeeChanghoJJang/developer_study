import json
import os 
#첫번째 방법
'''
os.chdir('./data/books')
file_names = os.listdir()
book_numbers = [os.path.splitext(filename)[0] for filename in file_names]
os.chdir('../')
os.chdir('../')

def new_books(book_numbers):
    book_2023 =[]
    for number in book_numbers:
        book_json = open(f'data/books/{number}.json', encoding='utf-8')
        book = json.load(book_json)
        if book['pubDate'][:4] == '2023':
            book_2023.append(book['title'])
    return book_2023[::-1]
'''
#두번쨰 방법
def new_books(books_list):
    book_2023 =[]
    for book in books_list:
        book_json= open(f'data/books/{book["id"]}.json',encoding='utf-8')
        book_file = json.load(book_json)
        if book_file['pubDate'][:4] == '2023':
            book_2023.append(book_file['title'])
    return book_2023[::-1]

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(new_books(books_list))