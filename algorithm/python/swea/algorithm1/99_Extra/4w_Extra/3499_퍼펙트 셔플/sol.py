import sys
import math
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    cards = list(input().split())
    result = []

    front = cards[:math.ceil(N/2)]
    end = cards[math.ceil(N/2):]
    for i in range(1,N+1):
        if i%2 ==1:
            result.append(front[(i-1)//2])
        elif i%2 ==0:
            result.append(end[(i-1)//2])
    print(f'#{tc}',end=' ')
    print(*result)
