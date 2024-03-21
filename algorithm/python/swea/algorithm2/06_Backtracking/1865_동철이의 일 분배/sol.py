import sys
sys.stdin = open('input.txt')

def dfs(start, result):
    global max_val
    if start == N:
        if max_val < result * 100:
            max_val = round(result * 100, 6)
        return

    if result * 100 < max_val or result == 0:
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(start + 1, result * arr[start][i])
            visited[i] = 0

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [tuple(map(lambda x: int(x) / 100, input().split())) for _ in range(N)]
    visited = [0] * N
    max_val = 0
    dfs(0, 1)
    print(f'#{tc} {max_val:.6f}')
