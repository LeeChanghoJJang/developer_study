import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    DP = [[0] * (N+1) for _ in range(N+1)]
    for i in range(1,N+1):
        DP[i][1] = DP[i-1][1] + arr[i-1][0]
    for i in range(1,N+1):
        DP[1][i] = DP[1][i-1] + arr[0][i-1]

    for i in range(2,N+1):
        for j in range(2,N+1):
            DP[i][j] = min(DP[i-1][j],DP[i][j-1]) + arr[i-1][j-1]
    print(f'#{tc} {DP[-1][-1]}')