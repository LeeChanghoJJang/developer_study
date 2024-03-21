### DP(Dynamic Programming)

#### 피보나치 수 적용 알고리즘

```python
def fibo2(n):
    f= [0] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2,n+1):
      f[i] = f[i-1] + f[i-2]

    return f[n]
```

- memoization을 재귀적 구조에 사용하는 것보다 반복적 구조로 DP를 구현한 것이 성능 면에서 보다 효율적이다.
```python 
def f(i, k):
  if i==k:
    print('end')
  else:
    f(i+1,k)
f(0,1000)
```

### 깊이 우선 탐색(DFS)
  - 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 다시 돌아와서 다른 방향의 정점으로 탐색 계속 반복하여 결국 모든 정점을 방문하는 순회방법(스택,재귀사용)
  
```python
visited[], stack[] 초기화
DFS(v)
  # 시작점 v 방문
  visited[v] # True로 처리
  while { 
    if # v의 인접 정점 중 방문 안한 정점 w가 있으면)
      push(v);
      v <- w;
      visited[w] # true
    else
      if (스택이 비어있지 않으면)
        v <- pop(stack)
      else
        break
  }
end DFS()
```
1. 정점 A를 시작으로 깊이 우선 탐색 시작
