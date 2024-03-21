import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    sequence = deque(map(int,input().split()))
    sequence.rotate(-(M%N))
    print(f'#{tc} {sequence[0]}')
