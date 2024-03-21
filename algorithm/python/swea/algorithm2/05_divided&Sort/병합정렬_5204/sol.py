import sys
sys.stdin = open('input.txt')

from collections import deque
# 병합정렬 함수 지정
def merge_sort(arr):
    if len(arr)==1:
        return arr
    # left, right 설정
    left,right = deque([]) , deque([])
    # 중간 이내는 좌측으로, 중간 이후는 우측으로
    for i in range(len(arr)):
        if i < len(arr)//2:
            left.append(arr[i])
        else:
            right.append(arr[i])
    # 좌측과 우측을 병합
    return merge(merge_sort(left),merge_sort(right))

def merge(left,right):
    global cnt
    # 좌측과 우측을 deque으로 설정
    left = deque(left)
    right = deque(right)
    result = []
    # 맨끝에꺼 비교해서 왼쪽이 크면 cnt 1증가
    if left[-1] > right[-1]:
        cnt+=1
    # left와 right 둘중하나가 없을때까지만
    while left and right:
        if left[0] <= right[0]:
            result.append(left.popleft())
        else:
            result.append(right.popleft())
    # 남은 것들은 result에 추가
    result.extend(left)
    result.extend(right)
    return result

for tc in range(1,int(input())+1):
    N = int(input())
    arr = deque(map(int,input().split()))
    cnt =0
    arr = merge_sort(arr)
    print(f'#{tc} {arr[N//2]}',end=' ')
    print(cnt)