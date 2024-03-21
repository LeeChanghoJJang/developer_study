queue = []
q = [0] * 10
front = rear = -1
# enqueue(10)
rear +=1
q[rear] =10
# enqueue(20)
rear +=1
q[rear] =20
# enqueue(30)
rear +=1
q[rear] =30
while front != rear:
    front +=1
    print(q[front])

from collections import deque
q = []
for i in range(200000):
    q.append(i)
print('append')
while q:
    q.pop(0)
print('end')

dq = deque()
for i in range(200000):
    dq.append(i)
print('append')
while dq:
    dq.popleft()
print('end')