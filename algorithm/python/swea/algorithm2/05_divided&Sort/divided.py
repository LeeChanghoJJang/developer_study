def divided(c,level):
    if level ==1:
        return c
    if level %2 ==0:
        return divided(c,level/2)*divided(c,level/2)
    else:
        return divided(c,(level-1)/2) * divided(c,(level-1)/2) * c

def merge_sort(m):
    if len(m)==1:
        return m
    left, right = [],[]
    middle = len(m)//2
    for x in m:
        if x < middle:
            left.append(x)
        else:
            right.append(x)
    return merge_sort(merge_sort(left),merge_sort(right))

def merge(left,right):
    result = []
    while len(left) >0 or len(right)>0:
        if len(left) > 0 and len(right) >0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left) >0:
            result.append(left.pop(0))
        elif len(right) >0:
            result.append(right.pop(0))
    return result 

# 퀵 정렬은 두 개로 분할하고 각각을 정렬한다.
# 병합 정렬은 그냐 두부분을 나누는 반면에, 퀵 정렬은 분할할 때 기준 아이템을 기준으로 분할

# 피봇 값들보다 큰 값은 오른쪽, 작은 값들은 왼쪽 집합에 위치하도록 한다.
# 피봇을 두 집합의 가운데 위치시킨다. 

# Lomuto partition
def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(r-1,-1,-1):
        if A[j] <= x:
            i +=1
            A[i], A[j] = A[j], A[i]
    A[i+1] , A[r] = A[r], A[i+1]
    return i+1

arr = [324,32,22114,16,48,93,422,21,316]
# 1. 정렬된 상태의 데이터
arr.sort()

# 2. 이진 검색 - 반복문 버전
def binarySearch(target):
    low=0
    high = len(arr) - 1
    # 탐색횟수
    cnt = 0
    # 해당 숫자를 찾으면 종료
    # 더 이상 쪼갤 수 없을 때까지
    while low <= high:
        mid = (low + high) // 2
        print(f'mid = {arr[mid]}')
        cnt +=1
        # 가운데 숫자가 정답이면 종료
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid -1
        elif arr[mid] > target:
            low = mid+1
    # 못찾으면 -1 반환
    return -1
# 이진검색 - 재귀함수 버전
def binarySearch2(low,high,target):
    # 기저조건 : 언제까지 재귀가 반복되어야 할까?
    if low > high:
        return -1
    
    # 다음 재귀 들ㅇ가기 전에 무엇을 해야할 까?
    # 정답 판별
    mid = (low + high) //2
    if target == arr[mid]:
        return mid
    # 다음 재귀함수에서 돌아왔을 때, 어떤 작어블 해야할까?
    if target < arr[mid]:
        return binarySearch2(low,mid-1,target)
    elif target > arr[mid]:
        return binarySearch2(mid+1,high,target)
    
print(f'21 = {binarySearch2(0,len(arr)-1,21)}')
print(f'324 = {binarySearch2(0,len(arr)-1,324)}')
print(f'93 = {binarySearch2(0,len(arr)-1,93)}')
print(f'888 = {binarySearch2(0,len(arr)-1,888)}')

