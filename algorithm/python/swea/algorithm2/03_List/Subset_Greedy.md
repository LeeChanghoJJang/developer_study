### 부분집합

> 부분집합에는 아무것도 선택하지 않는 경우도 포함됨.
> 집합의 원소를 선택하는 것 

### 구현하는 방법
> 완전탐색 (재귀호출 이용)
> Binary Counting(2진수 & 비트연산)

### 바이너리 카운팅
1. 2**n은 1<<n 공식을 이용해 빠르게 구할 수 있음
```python
arr = ['A','B','C']
n = len(arr)
def get_sub(tar):
    for i in range(n):
        if tar& 0x1:
            print(arr[i],end='')
        tar >>=1
for tar in range(1<<n):
    print('{',end=' ')
    get_sub(tar)
    print('}')
```

### 조합
> n개의 원소중 r개를 순서없이 골라낸 것을 조합이라고 함
```python
arr = ['A','B','C','D','E']
path = []
n = 3
def run(lev,start):
    if lev == n:
        print(path)
        return
    
    for i in range(start,5):
        path.append(arr[i])
```

### Greedy 
- 현재 기준으로 가장 좋아보이는 선택지 
- 결정이 필요할 때 가장 좋아보이는 선택지로 결정하는 알고리즘
```python
coin_list = [500,100,50,10]
tar = 1730
cnt = 0
for coin in coin_list:
    possiblecnt = tar // coin
    cnt += possiblecnt
    tar -= coin * possiblecnt
```
- Greedy 예외
- 만약 100원을 거슬러 주어야 하는경우, (10,50,70)
- 70먼저 나눠주면 그리디 미성립
- 모든 동전이 배수관계인 경우에는 그리디가 성립