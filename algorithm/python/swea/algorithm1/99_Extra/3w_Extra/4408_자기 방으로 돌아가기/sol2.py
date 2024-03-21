import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    corridor = [0] * 201
    N = int(input())
    cnt = 0
    for _ in range(N):
        front, end = map(int,input().split())
        min_val = int((front + 1) / 2)
        max_val = int((end + 1) / 2)
        for i in range(min_val,max_val +1):
            corridor[i] +=1
    print(f'#{tc} {max(corridor)}')

