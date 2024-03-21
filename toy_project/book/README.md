![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=300&section=header&text=Data%20Processing%20Using%20API%20&fontAlign=50&fontAlignY=30&fontColor=A3DCBE&fontSize=65&animation=scaleIn&desc=Book%20data%20collecton&descSize=40&descAlign=73&descAlignY=55)

![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)![markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)![visual studio code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![html](https://img.shields.io/badge/html-E34F26?style=for-the-badge&logo=html&logoColor=white)![css](https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css&logoColor=white)![bootstrap](https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)![scikit-learn](https://img.shields.io/badge/scikitlearn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)![plotly](https://img.shields.io/badge/plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
---


## 📶 목차
  - <span style="font-size:130%"> [학습 내용](#학습-내용)</span>
  - <span style="font-size:130%"> [어려운 점](#어려운-점)</span>
  - <span style="font-size:130%"> [보완점](#보완점)</span>
  
## ✍ 학습 내용 
  - <span style="font-size:120%"> **problem_a** : 샘플 도서 데이터(`json` 파일)에 있는 정보 추출하기
  </span>
  - <span style="font-size:120%"> **`problem_b`** : 카테고리 데이터를 활용하여 기존 도서 데이터의 categoryid를 categoryname으로 바꾸어 추출하기 </span>
  - <span style="font-size:120%"> **`problem_c`** : 하나의 데이터가 아닌 다중 데이터를 수정하여 필요한 정보만 추출하기</span>
  - <span style="font-size:120%"> **`problem_d`** : 도서의 `리뷰 평점`이 가장 높은 도서를 출력하는 알고리즘 작성</span>
  - <span style="font-size:120%"> **`problem_e`** : 도서의 `출판연도`를 이용하여 모든 도서 중 2023년에 출판한 도서들의 제목 출력하기 </span> 
  - <span style="font-size:120%"> **`problem_f1`** : 2023년 출판 도서 중 회원 리뷰 평점이 가장 높은 도서 제목 출력하기 </span>
  - <span style="font-size:120%"> **`problem_f2`** : 특정 카테고리의 도서들을 판매가격이 높은 순서대로 정렬한 리스트 출력하기 </span>

  ### Problem_a
  1. <span style="font-size:110%">`for` 반복문 또는 딕셔너리 컴프리헨션을 활용하여 딕셔너리 데이터 만들기</span>
  ```python
  # 반복문 이용
  new_dict ={}
  for i in ['author','categoryId','cover','description','id','priceSales','title']:
      new_dict[i]=book[i]
  # 딕셔너리 컴프리헨션
  new_dict = {i : book[i] for i in ['author','categoryId','cover','description','id','priceSales','title']}
  ```
  2. <span style="font-size:110%"> `json` 클래스를 이용하여 book_json 파일 데이터를 book 데이터에 저장하기</span>
  ```python
  book = json.load(book_json)
  ```

  ### Problem_b & Problem_c
  1. <span style="font-size:110%"> if문을 사용하여 `categoryid`와 일치하는 `name`을 추출하기 </span>
  ```python
  for i in new_dict['categoryId']:    
        for item in categories:
            if i == item['id']:
                temp.append(item['name'])
  ```
  ### Problem_d
  1. <span style="font-size:110%"> os 라이브러리를 이용하여 각 파일들을 오픈하기</span>
  ```python
  os.chdir('./data/books') # 경로변경
  file_names = os.listdir() # 현재 경로의 파일목록 저장
  # 확장자를 제외한 파일명들을 모아서 book_numbers에 저장
  book_numbers = [os.path.splitext(filename)[0] for filename in file_names]
  # 상위 폴더로 이동하여 원래 경로로 옮기기
  os.chdir('../')
  os.chdir('../')
  ```
  ### Problem_e
  1. <span style="font-size:110%"> 인덱싱과 슬라이싱을 활용하여 조건문 작성하기</span>
  ```python
    if book_file['pubDate'][:4] == '2023':
        book_2023.append(book_file['title'])
  ```
  2. <span style="font-size:110%"> 현재 순서를 역순으로 정렬하기</span>
  ```python
  return book_2023[::-1]
  ```
  ### Problem_f
  1. <span style="font-size:110%"> type 함수를 이용하여, 클래스가 `list`인지 `int`인지 판단 </span>
  ```python
  if type(book_file['categoryId']) == list:
            if category_id in book_file['categoryId']:
                price_books.update({book_file['title']:book_file['priceSales']})
  elif type(book_file['categoryId']) ==int:
      if category_id == book_file['categoryId']:
          price_books.update({book_file['title']:book_file['priceSales']})
  ```
  2. <span style="font-size:110%"> `sorted` 함수를 이용하여 `list`의 순서를 조정 </span>
  ```python
  sorted(list(price_books),key = lambda x : x[1])
  ```
  
## 🤣 어려운 점
  - <span style="font-size:120%"> 데이터 추출보다 **원하는 형태**로 가공하는 것이 어려움</span>
  - <span style="font-size:120%"> 용어가 어려워 해당 분야에 대한 이해가 선행되어야 함을 느낌 
  </span>

## 🚀 보완점
  - <span style="font-size:120%"> 데이터를 파악할 때 하나씩 출력하면서 json 데이터의 형태와 신속하게 키값을 찾는 것이 중요 
  </span>
  - <span style="font-size:120%"> 시간이 많이 걸리는 데이터 수집을 간단하게 했음에도 불구하고, 많은 시간이 소요되어 신속한 코드 작성 필요 
  </span>
