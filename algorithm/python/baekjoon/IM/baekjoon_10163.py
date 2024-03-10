import sys
sys.stdin=open('input.txt')

def coloring(x1,y1,x2,y2,color):
    for i in range(x1, x2):
        arr[i][y1:y2]=[color]*(y2-y1)

def counting(arr,color):
    cnt = 0
    for i in range(1001):
        cnt+= arr[i].count(color)
    return cnt


arr = [[0] * 1001 for _ in range(1001)]
color = 1
T = int(input())
for tc in range(T):
    x1,y1,x1_alpha,y1_alpha = map(int,input().split())
    coloring(x1,y1,x1 + x1_alpha,y1 + y1_alpha ,color)
    color += 1
for i in range(T):
    print(counting(arr,i+1))
