import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        graph[start][end]=1
    S,G = map(int,input().split())
    cnt=0
    temp = [S]
    while temp:
        now = temp.pop()
        if now == G:
            cnt =1
            break
        for arrives in range(1,V+1):
            if graph[now][arrives]:
                temp.append(arrives)
    print(f'#{tc} {cnt}')