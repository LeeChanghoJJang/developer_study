import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc}')
    for row in range(N):
        for col in range(N):
            print(arr[N-1-col][row],end='')
        print(' ',end='')
        for col in range(N):
            print(arr[N-1-row][N-1-col],end='')
        print(' ',end='')
        for col in range(N):
            print(arr[col][N-1-row],end='')
        print()