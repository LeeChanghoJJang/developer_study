### 백트래킹

> 정의 : 해를 찾는 도중에 `막히면` 되돌아가서 다시 해를 찾아가는 기법
  - 최적화 문제와 결정문제 해결가능
  - 결정문제 : 미로찾기, n-queen문제, map coloring, 부분집합의 합문제

#### 백트래킹과 깊이 우선 탐색과의 차이
> 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 회수를 줄임(가지치기)
> 깊이우선탐색이 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로 조기 차단
> 깊이우선탐색을 가하기에는 경우의 수가 너무나 많음
> 즉 N! 가지의 경우의 수를 가진 문제에 대해 깊이우선탐색을 가하면 당연히 처리 불가능한 문제.
> 백트래킹을 적용하면 경우의 수가 줄어들지만 이 역시 최악의 경우에는 지수함수의 시간 요

#### 백트래킹 기법
> 어떤 노드의 유망성을 점검한 후에 유망(promising)하지 않다고 결정되면 그 노드의 부모로 되돌아가(backtracking) 다음 자식 노드로 감
> 어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며, 반대로 해답의 가능성이 있으면 유망하다고 함
> 가지치기 : 유망하지 않는 노드가 포함되는 경로는 더이상 고려하지 않는다.

#### 백트래킹 절차
> 상태 공간 트리의 깊이 우선 검색을 실시
> 각 노드가 유망한지 점검
> 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색 지속 

```python
def checknode(v) # node
  if promising(v):
    if there is a solution at v:
      write the solution
    else:
      for u in each child of v:
        checknode(u)
```

#### 부분집합
> 어떤 집합의 원소 개수 : n ==> 2의 n승
```python
# `powerset`을 구하는 백트래킹 알고리즘
def backtrack(a.k.input):
  global MAXCANDIDATES
  c = [0] * MAXCANDIDATES
  
  if k == input:
    process_solution(a,k)
  else:
    k +=1
    ncandidates = construct_candidates(a,k,input,c)
    for i in range(ncandidates):
      a[k] = c[i]
      backtrack(a,k,input)

def construct_candidates(a,k,input,c):
  c[0] = True
  c[1] = False
  return 2

MAXCANDIDATES = 2
NMAX = 4
a = [0] * NMAX
backtrack(a,0,3)
```

#### 순열 구하기
```python
def backtrack(a,k,input):
  global MAXCANDIDATES
  c = [0] * MAXCANDIDATES
  
  if k == input:
    for i in range(1,k+1):
      print(a[i],end=' ')
    print()
  else:
    k+=1
    ncandidates = construct_candidates(a,k,input,c)
    for i in range(ncandidates):
      a[k] = c[i]
      backtrack(a,k,input)
      
def construct_candidates(a,k,input,c):
  in_perm = [False] * NMAX
  
  for i in range(1,k):
    in_perm[a[i]] = True

  ncandidates = 0
  for i in range(1, input +1):
    if in_perm[i] == False:
      c[ncandidates] = i
      ncandidates += 1
  return ncandidates

```