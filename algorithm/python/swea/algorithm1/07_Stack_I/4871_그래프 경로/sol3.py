import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    # 루트 입력 -> 예시 : [[],[4,3],[3,5],[],[6],[]]
    routes = [[] for _ in range(V+1)]
    for _ in range(E):
        s,e = map(int,input().split())
        routes[s].append(e)
    print(routes)
    # 시작점, 도착점
    start,end = map(int,input().split())
    # 방문 장소 체크
    visit = [0] * (V+1)
    # 스택 시작점 할당
    stack = [start]
    # 답
    is_exist = 0

    # DFS : 스택에 원소가 없거나 도착점에 도달하면 종료
    while stack:
        now = stack[-1]
        if now == end:
            is_exist = 1
            break

        # 현재점과 연결된 도착점 파악
        for next in routes[now]:
            if not visit[next]:
                visit[now] = 1
                stack.append(next)
                break
        else:
            visit[now]=1
            stack.pop()

    print(f'#{tc} {is_exist}')
