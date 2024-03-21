import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    A = tuple(map(int, input().split()))
    B = tuple(map(int, input().split()))
    if N>M:
        N,M = M,N
        A,B = B,A
    temp = []
    for i in range(M-N+1):
        result = 0
        for j in range(N):
            result += A[j] * B[i + j]
        temp.append(result)

    print(f'#{tc} {max(temp)}')