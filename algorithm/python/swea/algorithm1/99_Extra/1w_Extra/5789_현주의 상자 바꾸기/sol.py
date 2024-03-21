import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    N,Q = map(int,input().split())
    temp = [0]*N
    for number in range(1,Q+1):
        L,R = map(int,input().split())
        for box in range(L-1,R):
            temp[box] = number
    print(f'#{tc}',end=' ')
    print(*temp)

