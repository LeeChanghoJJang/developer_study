'''
9
7 4 2 0 0 6 0 7 0
'''
N = int(input()) # 상자가 쌓여있는 가로 길이
arr = list(map(int, input().split()))

max_v = 0 # 가장 큰 낙차
for i in range(N-1): #for i : 0 -> N-2
    cnt = 0 # 오른쪽에 있는 더 낮은 높이의 개수
    for j in range(i+1,N): # for j : i+1 -> N+1
       if arr[i] > arr[j]:
           cnt +=1
    if max_v < cnt: # 최대 낙차보다 크면
        max_v = cnt
print(max_v)
arr = [7,4,5,2,1,3]
N=6
def asc(arr,N):
    for i in range(N-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
def dec(arr,N):
    for i in range(N-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
print(asc(arr,N))
print(dec(arr,N))
