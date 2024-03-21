import sys
sys.stdin = open('input.txt')

def binary_search(arr,arr2):
    global cnt
    for target in arr2:
        left, right = 0, len(arr)-1
        dir = 0
        while left <= right:
            middle = (left + right) // 2
            if target == arr[middle]:
                cnt +=1
                break
            elif target > arr[middle]:
                left = middle + 1
                if dir == 1:
                    break
                dir = 1
            elif target < arr[middle]:
                right = middle - 1
                if dir == -1:
                    break
                dir = -1

for tc in range(1,int(input())+1):
    N,M = map(int,input().split())
    A = sorted(map(int,input().split()))
    B = list(map(int,input().split()))
    cnt = 0
    binary_search(A, B)
    print(f'#{tc} {cnt}')