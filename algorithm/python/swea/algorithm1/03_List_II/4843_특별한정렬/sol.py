import sys
sys.stdin = open('input.txt')

# bubble정렬 이용
def bubble_sort(arr):
    # arr의 길이 도출
    cnt =0
    for i in arr:
        cnt += 1
    # 순회할 때마다 길이 i 지정
    for i in range(cnt-1,-1,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# counting 정렬 이용
def counting_sort(arr):
    # arr의 길이 및 최댓값 도출
    cnt = 0
    max_value = 0
    for i in arr:
        cnt += 1
        if i > max_value:
            max_value = i

    # 카운팅정렬 정의
    count_arr = [0]*(max_value+1)

    # arr의 원소들의 갯수만큼 count_arr 채우기
    for i in arr:
        count_arr[i] +=1
    # count_arr 누적합 구하기 (count_arr의 인덱스가 원래 값이며, 값은 원래 위치가 반영됨)
    for i in range(1,max_value+1):
        count_arr[i] += count_arr[i-1]

    temp=[0] * cnt
    for i in arr:
        count_arr[i]-=1
        temp[count_arr[i]] = i
    return temp

def selection_sort(arr):
    # arr의 길이 도출
    cnt = 0
    for i in arr:
        cnt += 1
    # 길이만큼 순회
    for i in range(cnt):
        for j in range(i+1, cnt):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr

# 실행코드
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    # 문제에서 주어지는 배열을 오름차순으로 정렬하여 할당
    arr = sorted(list(map(int,input().split())))
    # arr = bubble_sort(list(map(int, input().split())))
    # arr = counting_sort(list(map(int, input().split())))
    # arr = selection_sort(list(map(int, input().split())))
    temp = []
    # 가장 큰값, 가장 작은값, 두번째 큰값, 두번째 작은값, ... 순
    # 가장 큰값과 가장 작은값을 배열에서 제외하면,
    # 두번째 큰값도 결국 그 배열에서 가장 큰값이 되는 점을 이용
    # 가장 큰값과 작은값 총 10개 출력위해 5번만 순회
    for _ in range(5):
        # pop을 이용해 max와 min값을 추출
        max_num=arr.pop()
        min_num=arr.pop(0)
        temp.extend([max_num,min_num])
    print(f'#{tc}',end=' ')
    print(*temp)

