from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
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
            book_list = [books['title'],
                        books['author']
            ]
            temp.append(book_list)

        return temp
    temp = new_books(data)
    context = {
        'temp':temp
    }
    return render(request,'recommend.html',context)