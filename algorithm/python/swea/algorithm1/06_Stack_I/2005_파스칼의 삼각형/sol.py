import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    print(f'#{tc}')
    N = int(input())
    arr = [[1] * (N+1) for _ in range(N+1)]

    for i in range(1,N+1):
        for j in range(1,i):
            arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

    for i in range(N):
        for j in range(i+1):
            print(arr[i][j],end=' ')
        print()
