def deadlock(arr,N):
    cnt = 0
    # 교착상태를 이용하기 위한 리스트를 담자
    for col in range(N):
        temp = []
        for row in range(N):
            # 1인 이후 2가 발견되면 cnt를 추가할 것.
            if arr[row][col]==1 and not temp:
                temp.append(1)
            # 숫자가 2이면 temp의 마지막 숫자가 1일때 cnt 추가
            elif temp and arr[row][col]==2:
                cnt+=temp.pop()
    return cnt

for tc in range(1,11):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 1은 빨간색, 2는 파란색
    print(f'#{tc} {deadlock(arr,N)}')