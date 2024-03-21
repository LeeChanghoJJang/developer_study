# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

import sys
sys.stdin = open('input.txt')

def solution(k): # 할일이 노드번호를 출력하는 것
    print(k,end=' ')

def preorder(now): #조사시작 노드 번호부터 조사를 시작한다.
    # 노드 번호는 없음!
    if now !=0:
        # 전위 순회는, 조사 시작 노드 번호에 대해서 할 일을 수행
        solution(now)
        # 왼쪽자식 순회
        preorder(tree[now][0])
        # 오른쪽자식 순회
        preorder(tree[now][1])

def inorder(now):
    if now !=0:
        inorder(tree[now][0])
        solution(now)
        inorder(tree[now][1])

def postorder(now):
    if now != 0:
        postorder(tree[now][0])
        postorder(tree[now][1])
        solution(now)

V = int(input())
edge = list(map(int,input().split()))
print(edge)
E = len(edge) # 간선 정보 길이
# 인접 리스트
# adj = [[] for _  in range(V+1)] # 0번 노드는 없다
# tree[현재 노드 번호][0] -> 현재 노드 번호의 왼쪽 자식 노드 번호
tree = [[0,0] for _ in range(V+1)]
# print(tree)
for idx in range(E//2):
    # 특정 위치에 값을 할당하는 것.
    if tree[edge[idx*2]][0] ==0:
        # 왼쪽 자식이 없다면  
        tree[edge[idx*2]][0] = edge[idx*2+1]
    else:
        # 왼쪽 자식이 있다면
        tree[edge[idx*2]][1] = edge[idx*2+1]
# print(tree)
# for idx in range(E//2):
#     adj[edge[idx*2]].append(edge[idx*2+1])

preorder(1)
print()
inorder(1)
print()
postorder(1)