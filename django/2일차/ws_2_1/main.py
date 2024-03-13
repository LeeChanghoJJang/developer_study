import requests
from pprint import pprint
URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = ''
params = {
    'ttbkey': API_KEY,
    'QueryType' : 'ItemNewSpecial',
    'MaxResults' :50,
    'start':1,
    'SearchTarget':'Book',
    'output':'js',
    'Version':'20131101'
}

data = requests.get(URL,params=params).json()
def new_books(data):
    temp = []
    for i in range(50):
        books = data['item'][i]
        book_list = {'국제 표준 도서 번호':books['isbn'],
                    '저자':books['author'],
                    '제목':books['title'],
                    '출간일':books['pubDate']  
        }
        temp.append(book_list)
    
    return temp
pprint(new_books(data))