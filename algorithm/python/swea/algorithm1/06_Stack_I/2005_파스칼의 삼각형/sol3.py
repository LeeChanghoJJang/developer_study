import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1,T+1):
    print(f'#{tc}')
    N = int(input())
    memo = [[1] * 10 for _ in range(10)]

    for i in range(1,10):
        for j in range(1,10):
            if i !=j:
                memo[i][j] = memo[i-1][j-1] + memo[i-1][j]
    print(memo)

