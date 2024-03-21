import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    # 특징 1. 목적지 > 출발점
    # 특징 2. 짝수면 출발점 -1. 도착점 -1
    corridor = [0] * 402
    N = int(input())
    cnt = 0
    for _ in range(N):
        start, end = map(int, input().split())
        start = min(start,end)
        end = max(start,end)
        if start %2==0: start-=1
        if end %2==0: end-=1
        for i in range(start,end+1):
            corridor[i] +=1
    print(f'#{tc} {max(corridor)}')