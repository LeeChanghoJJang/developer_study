### 2차원 배열

1. 정의
    - 1차원 List를 묶은 List
    - Python에서는 데이터 초기화를 통해 변수 선언과 초기화 가능
    
2. 예시
```python
N= int(input)
arr = [list(map(int, input().split())) for _ in range(N)]
arr2 = [[0] * N for _ in range(N)]
# 이거는 하지 말라고 보여주는 것 
arr3 = [[0]*N]*N
arr3[0][0] =1 
'''
arr3[0][0] =1을 넣으면 아래와 같이 변함
1 0 0
1 0 0
1 0 0
'''
```
3. 배열 순회
```python
def function(arr):
    return arr
n=m=10
arr=[0]*n
# 행 우선순회 -> 열 우선순회는 i와 j를 바꾸면 됨
for i in range(n):
    for j in range(m):
       function(arr[i][j]) # 필요한 연산 수행
# 지그재그 순회 
for i in range(n):
    for j in range(m):
       function(arr[i][j + (m-1-2*j)*(i%2)])
# 델타를 이용한 2차 배열 탐색
dx = [0,1,0,-1]
dy = [1,0,-1,0]
x,y=0
for k in range(n):
    x += dx[0]
    y += dy[0]
```
```python
N = 5
arr = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<N:
                print(arr[ni][nj],end=' ')
# 각 위치마다 델타만큼 이동 
```
```python
# i : 행의 좌표, len(arr)
# j : 열의 좌표, len(arr[0])
arr =[[1,2,3],[4,5,6],[7,8,9]] # 3*3행렬
for i in range(3):
    for j in range(3):
        if i<j:
            arr[i][j],arr[j][i] = arr[j][i],arr[i][j] 
```

#### 부분집합의 합 
1. 방법
   - 완전검색 기법으로 부분집합을 모두 구해야함 
   - 부분집합 모두 구하고 나서 합을 도출
```python
arr = [1,3,5,4,6,12,36,47,57]
N = 9
total = []
for i in range(1<<N):
    temp = []
    for j in range(N):
        if i&(1<<j):
            temp.append(j)
    total.append(temp)
```   
#### 순차검색
- 정의 : 일렬로 되어 있는 자료를 순서대로 검색하는 방법
   1. 가장 간단하고 직관적인 검색 방법
   2. 배열이나 연결 리스트 등 순차구조로 구현된 자료 구조에서 원하는 항목을 찾을 때 유용
   3. 알고리즘이 단순하여 구현이 쉽지만, 검색 대상의 수가 많은 경우 비효율적

- 첫번째 원소 찾을 때 1번 비교 두번째 원소 찾을 때 2번 비교 : n(n+1)/2번
- 정렬되지 않은 자료에서의 순차 검색의 평균 비교 횟수 : (1/n) * n(n+1)/2 = (n+1)/2
> 즉 하나의 원소를 찾고자 할 때 시간복잡도는 O(n)
```python
def sequential_search(a,n,key):
    i =0
    # out of range Error 방지 위함 
    while i<n and a[i]!=key:
        i +=1
    if i<n: return i
    else: return -1
```
- 정렬되어 있는 경우
> 찾았을 경우에는 정렬되지 않은 것과 동일
> 검색 실패를 반환하는 경우 평균 비교 회수가 반으로 줆
```python
def sequential_search(a,n,key):
    i =0
    # out of range Error 방지 위함 
    while i<n and a[i]<key:
        i +=1
    if i<n and a[i]==key: return i
    else: return -1
## 내가 생각한 코드
def sequential_search(a,n,key):
    for i in range(n):
        if a[i] ==key:
            return i
        else:
            return -1
```

#### 이진 검색
- 순서
    1. 자료 중앙의 원소를 고른다
    2. 중앙 원소의 값과 찾고자 하는 목표값을 비교
    3. 목표값이 중앙 원소값보다 작으면 자료의 왼쪽 반에 대해 새로 검색, 크다면 자료의 오른쪽 반에 대해 새로 검색
    4. 찾고자 하는 값을 찾을 때까지 1~3을 반복
```python
# 내 코드(단순히 활용하는 것이면 edge값 안중요하지만,
# 문제에서 주어지는 경우에는 문제를 따라 결정
def binarysearch(arr, N, key):
    # 정렬안됬을 때
    start = 0
    end = N-1
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] ==key:
            return mid
        elif arr[mid] < key:
            start= mid+1
        elif arr[mid] > key:
            end = mid-1
    return False

def binarysearch2(a,low,high,key):
    if low >high: return False
    else:
        middle = (low+high)//2
        if key == a[middle]:
            return True
        elif key < a[middle]:
            return binarysearch2(a,low,middle-1,key)
        elif key > a[middle]:
            return binarysearch2(a,middle+1,high,key)
```
#### 인덱스
- 정의 : DataBase에서 유래 햇으며, 테이블 동작 속도를 높여주는 자료구조
- 인덱스를 저장하는데 필요한 디스크 공간은 보통 테이블을 저장하는데 필요한 디스크공간보다 작다.
- 왜냐면 보통 인덱스는 키-필드만 갖고 있고, 테이블의 다른 세부 항목들은 갖고 있지 않기 때문이다
> 그렇기에 상대적으로 크기작은 인덱스 배열을 정렬하는 게 더 속도가 빠르다.

#### 선택정렬
- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식
- 순서
    1. 주어진 리스트에서 최솟값을 찾는다.
    2. 리스트의 맨 앞 위치한 값과 교환한다.
    3. 맨앞 최솟값을 제외하고 나머지 미정렬 리스트에서 위 과정 반복한다.
    4. 원소 2개남았을 때까지 한다.
> k가 비교적 작을 때 유용하며, O(kn)의 수행시간 필요
> 평균 수행시간은 O(n**2)
> 
```python
def SelectionSort(arr,N):
    # 주어진 구간의 시작
    for i in range(N-1):
        # i가 젤 작은 값이라고 가정
        min_idx = i
        # 미정렬 리스트(i+1부터 n까지) 순회 
        for j in range(i+1,N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        # 젤 최소값을 미정렬 리스트의 젤 첫원소랑 교환        
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
N=5
arr = [-1,3,-2,5,2]
print(arr)
SelectionSort(arr,N)
```
# 1964 달팽이 숫자
# 연습문제 3 : 2차원 배열 흩뜨려진거 초기화한 후, 정렬
