import sys
sys.stdin = open('input.txt')
# 퀵정렬
def quick(arr):
    # 길이가 1보다 작을 때에는 1개원소 반환
    if len(arr) <= 1:
        return arr
    # 피봇은 중간위치에 있는 원소로 설정
    pivot = arr[len(arr) // 2]
    # 피봇보다 작고 같고 큰 리스트를 각각 지정
    less, equal, greater = [],[],[]
    # 피봇과 비교해서 작거나 같거나 큰것들을 따로 분류
    for num in arr:
        if num < pivot:
            less.append(num)
        elif num > pivot:
            greater.append(num)
        else:
            equal.append(num)
    # 재귀함수를 써서 한개가 남을 때까지 하면 밑에서부터 정렬되서 올라옴
    return quick(less) + equal + quick(greater)

for tc in range(1,int(input())+1):
    N = int(input())
    arr = list(map(int,input().split()))
    print(f'#{tc} {quick(arr)[N//2]}')
