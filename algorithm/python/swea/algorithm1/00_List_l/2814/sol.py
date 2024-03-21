import sys
sys.stdin = open('input.txt')
dx = [0,1,0,-1]
dy = [1,0,-1,0]
# DFS 사용해보장
def max_street(now,M,result,arr):
    global max_val
    if M== 0:
        return 1
    if max_val > result:

    stack = [now]
    while stack:
        now = stack[-1]
        visited[now] += 1
        for next in arr[now]:
            if not visited[next]:
                visited[next] = visited[now]
                stack.append(next)
                break
        else:
            stack.pop()
    return max(visited)

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    for _ in range(M):
        # x,y 는 서로 다른 정수
        x,y = map(int,input().split())
        arr[x].append(y)
        arr[y].append(x)
    print(f'#{tc} {max_street(1,M,arr)}')
