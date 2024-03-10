# 백준 2751번 수 정렬하기 2
import sys
sys.stdin = open('input.txt')
# 첫번째 코드 : 84788KB 1432ms
# N=int(input())
# temp=[]
# for i in range(N):
#     temp.append(int(sys.stdin.readline()))
# for i in sorted(temp):
#     print(i)
# 두번째 코드 : Bubble Sort (해결 불가)- O(N**2)
# N = int(input())
# arr = [int(input()) for _ in range(N)]
# for i in range(N):
#     for j in range(N-1):
#         if arr[j] > arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1],arr[j]
# 세번째 코드 : Merge Sort -
N = int(input())
arr = [int(input()) for _ in range(N)]
def mergesort(list):
    size = len(list)
    if size <= 1: return list

    mid = len(list) // 2
    left = mergesort(list[:mid])
    right = mergesort(list[mid:])
    merged = merge(left,right)
    return merged

def merge(list1,list2):
    merged = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] <= list2[0]:
            merged.append(list1.pop(0))
        else:
            merged.append(list2.pop(0))
    if len(list1) > 0:
        merged += list1
    if len(list2) < 0 :
        merged += list2
    return merged

for i in mergesort(arr):
    print(i)
