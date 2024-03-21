import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N,M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0,1,0,-1]
    dy = [-1,0,1,0]

    result_sum = 0
    for x in range(N):
        for y in range(M):
            max_sum = arr[x][y]
            for j in range(1,max_sum+1):
                for i in range(4):
                    nx = x + dx[i] * j
                    ny = y + dy[i] * j
                    if 0<=nx<N and 0<=ny<M:
                        max_sum += arr[nx][ny]
            if result_sum < max_sum:
                result_sum = max_sum
    print(f'#{tc} {result_sum}')