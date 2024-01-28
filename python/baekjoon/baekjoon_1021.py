# 1021번 회전하는 코드 
# 내코드
from collections import deque
N,M = map(int,input().split())
order = list(map(int,input().split()))
queue = deque(range(1,N+1))
cnt=0
# N으로 큐를 만들기
# order의 순서대로 넘버를 뽑은 후, 그 order가
while order:
    number = order.pop(0)
    find_witch = queue.index(number)
  
    if find_witch > len(queue)//2:
        queue.rotate(len(queue) - find_witch)
        cnt += len(queue) - find_witch
    elif find_witch <= len(queue)//2:
        queue.rotate(-1 * find_witch)
        cnt+=find_witch
    queue.popleft()  
print(cnt)

'''
다른 코드와 달리 while문 반복 횟수를 줄이기 위해 
rotate시, 횟수를 곱했음 
'''
