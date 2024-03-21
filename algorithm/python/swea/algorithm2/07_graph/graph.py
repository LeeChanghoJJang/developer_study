# 그래프 : 데이터간 관계를 표시하기 위해 노드와 간선으로 이뤄진 자료구조

# 그래프는 아이템들과 이들 사이의 연결 관계를 표현
'''
그래프는 정점들의 집합과 이들을 연결하는 간선들의 집합으로 구성됨
V : 정점의 개수 / E : 그래프에 포함된 간선의 개수
'''
# 그래프 유형 : 무향 - 유향 그래프, 가중치 그래프, 사이클 없는 방향 그래프

# 1. 그래프를 코드로 표현 
# - 인접 행렬
#    - V x V 배열을 활용해서 표현
#    - 갈 수 없다면 0, 있다면 1(가중치)을 저장
# 특징 : 양방향 그래프는 중앙 우하단 대가선 기준으로 대칭됨
# - 장점
#   - 노드 간의 연결 정보를 한 방에 확인 가능
#   - 간선이 많을수록 유리
#   - 행렬곱을 이용해서 탐색이 쉽게 가능하다.
# - 단점
#   - 노드 수가 커지면 메모리가 낭비된다
#   - 연결이 안된 것도 저장하기 때문
#   - 메모리 제한 256MB
graph = [[0, 1, 0, 1, 0],
         [1, 0, 1, 0, 1],
         [0, 1, 0, 0, 0],
         [1, 0, 0, 0, 1],
         [0, 1, 0, 1, 0]]
# - 인접 리스트
#   - V 개의 노드가 갈 수 있는 정보만 저장
# - 장점
#   - 메모리 사용량이 적다
#   - 탐색할 때 갈 수 있는 곳만 확인하기 때문에 시간적으로 효율
# - 단점
#   - 특정 노드간 연결 여부 확인하는데 시간이 걸린다.
graph = [
    [1,3],
    [0,2,4],
    [1],
    [0,4],
    [1,3],
]
path=[]
visited=[0] * 5

def dfs(now):
    # 기저 조건
    # 지금 문제에서는 없다!

    # 다음 재귀 호출 전
    print(now,end=' ')
    # 다음 재귀 호출
    # dfs: 현재 노드에서 다른 노드들을 확인
    # 다른 노드들 == 반복문
    for to in graph[now]:
        # 갈 수 없다면 pass
        if visited[to]:
            continue
        
        visited[to]=1
        path.append(to)
        dfs(to)
visited[0]=1
path.append(0)
dfs(0)

def bfs(start):
    visited = [0]*5
    # 시작노드를 큐에 추가 + 방문 표시
    queue = [start]
    visited[start]=1

    while queue:
        now = queue.pop(0)
        print(now,end=' ')

        # 갈 수 있는 곳을 체크
        for to in range(5):
            if graph[now][to] ==0:
                continue

            if visited[to]:
                continue
            visited[to] = 1
            queue.append(to)

# 서로소 집합(Disjont-sets)
# 서로소 또는 상호배타 지합들은 서로 중복 포함된 원소가 없는 집합들. 
# 다시말해 교집합이 없다
# 집합에 속한 하나의 특정 멤버를 통해 각 집합들을 구분한다. 이를 대표자라 한다.

# 상호배타 집합을 표현하는 방법 - 연결 리스트, 트리
# 상호배타 집합 연산 : Make-Set(x), Find-Set(x), Union(x,y)   

# 상호배타 집합을 표현한 트리의 배열을 이용한 저장된 모습

# 1.make_set
def make_set(n):
    return [ i  for i in range(n)]
# 2.find_set : 대표자를 찾아보자
# - 부모 노드를 보고, 부모 노드도 연결이 되어 있다면 다시 반복
# - 언제까지 ? 자기자신이 대표인 데이터를 찾을 때까지
parents = make_set(7)
def find_set(x):
    if parents[x] != x:
        parents[x] = find_set(parents[x])
    return parents[x]
    # # 자기 자신이 대표네? 끝
    # if parents[x] == x:
    #     return x
    # # 위의 조건이 걸리지 않았다 == 대표자가 따로 있다.
    # return find_set(parents[x])
# 3. union
rank = [0] * N
def union(x,y):
    root_x = find_set(x)
    root_y = find_set(y)
    # 이미 같은 집합에 속해있다면 continue
    # if x==y:
    #     return 
    # if x<y:
    #     parents[y]=x
    # else:
    #     parents[x]=y

    if root_x != root_y:
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] +=1

union(1,3)
print(parent)
print(rank)
union(2,3)
union(5,6)
