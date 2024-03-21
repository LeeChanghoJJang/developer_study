import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    container = sorted(map(int,input().split()))
    truck = sorted(map(int,input().split()))
    result =0
    while container and truck:
        if truck[-1] >= container[-1]:
            truck.pop()
            result+=container.pop()
        else:
            container.pop()
    print(f'#{tc} {result}')