import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    corridor = [0] * 201
    N = int(input())
    cnt = 0
    for _ in range(N):
        now, back = map(int, input().split())
        mins = (min(now,back)+1)//2
        maxs = (max(now,back)+1)//2
        for i in range(mins,maxs+1):
            corridor[i] +=1
    print(f'#{tc} {max(corridor)}')
