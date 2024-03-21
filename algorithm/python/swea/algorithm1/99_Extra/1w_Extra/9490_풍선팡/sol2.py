import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    max_sum = 0
    for x in range(N):
        for y in range(M):
            sum_val = arr[x][y]
            for plus in range(1,arr[x][y]+1):
                for i in range(4):
                    nx = x + dx[i]*plus
                    ny = y + dy[i]*plus
                    if 0<=nx<N and 0<=ny<M:
                        sum_val += arr[nx][ny]

            if max_sum < sum_val:
                max_sum = sum_val
    print(f'#{tc} {max_sum}')
