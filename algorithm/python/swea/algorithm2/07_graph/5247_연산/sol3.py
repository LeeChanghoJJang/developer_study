import sys
sys.stdin = open('input.txt')
from collections import deque

for tc in range(1,int(input())+1):
    N, M = map(int, input().split())
    DP = [int(1e6)] * 1000000
    DP[N] = 0
    queue = deque([N])
    for i in range(N):
        DP[i] = N - i

    for i in range(N + 1, 2 * K + 1):
        if i % 2 == 0:
            DP[i] = min(DP[i // 2] + 1, DP[(i - 1)] + 1)
        else:
            DP[i] = min(DP[(i - 1) // 2] + 2, DP[(i + 1) // 2] + 2, DP[i - 1] + 1)
    print(DP[K])

