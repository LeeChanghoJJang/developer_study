# 1. 전체 그래프를 보고, 가중치가 제일 작은 간선부터 뽑자.
# -> 코드로 구현 : 전체 간선 정보를 저장 + 가중치로 정렬

# 2. 방문 처리
#   -> 이 때, 싸이클이 발생하면 안된다!
#   -> 싸이클 여부 ?? ==> union-find 알고리즘 활용

import sys
sys.stdin = open('input.txt')
def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x,y):
    x = find_set(x)
    y = find_set(y)
    if x==y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

V, E = map(int,input().split())
edges = []

for _ in range(E):
    s, e, w = map(int,input().split())
    edges.append([s,e,w])
edges.sort(key=lambda x:x[2])
parents = [i for i in range(V)]

cnt = 0
sum_weight = 0
for s,e,w in edges:
    # 싸이클이 발생하면 pass
    # -> 이미 같은 집합에 속해 있다면 pass
    if find_set(s) == find_set(e):
        print(s,e)
        continue
    # 싸이클이 없으면 방문 처리
    union(s, e)
    sum_weight += w

    if cnt == V - 1: # 최소 신장트리 완성
        break

print(f'최소 비용 = {sum_weight}')