from collections import deque
import sys
sys.stdin = open('input.txt')

for _ in range(1,11):
    tc = int(input())
    queue = deque(map(int,input().split()))
    check = True
    while 1:
        for i in range(1,6):
            queue[0] -= i
            if queue[0] < 0:
                queue[0] = 0
            queue.rotate(-1)
            if queue[-1] ==0:
                check =False
                break
        if check==False:
            break
    print(f'#{tc}', end=' ')
    print(*queue)

