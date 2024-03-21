import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())
    graph = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        a,b= map(int,input().split())
        graph[a][b]=1
    S, G =map(int,input().split())
    temp = [S]
    check=False
    while temp:
        print(temp)
        x = temp.pop()
        for i in range(V+1):
            if graph[x][i]==1:
                temp.append(i)
                if i == G:
                    check = True
                    break
        if check:
            break
    print(f'#{tc} {int(check)}')