import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1,T+1):
    N= int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 초기값 설정
    min_sum=float('inf')
    # 백트래킹 함수 정의
    def backtracking(row,result,visited):
        # 최소값을 구하기 위해 전역변수로 설정
        global min_sum
        # N개의 합을 구하고, 그것이 지금까지 최소값보다 더 작으면 그걸로 갱신
        if row == N and min_sum > result:
            min_sum = result
            return
        # row는 순차적으로 재귀함수를 통해 순회 중이며,
        # 해당 row에 모든 col을 봤을 때, 안겹치는 경우만 그 다음 함수 호출
        for col in range(N):
            # result값에 저장된 값이 지금까지 최소값보다 작을때만
            # 현재까지 visited에 저장된 col과 겹치면 안됨
            if result + arr[row][col] < min_sum and col not in visited:
                # 현재까지 방문된 col을 저장해두고 안겹치는 열만 추출하기 위함
                visited.add(col)
                # 문제의 조건을 충족한 경우 다음 row에서 col을 뽑기 위해 재귀함수 호출
                backtracking(row+1,result+arr[row][col],visited)
                # 백트래킹하기 위해 한번 연산이 끝나면 col 순차적 제거
                visited.remove(col)

    backtracking(0,0,set())
    print(f'#{tc} {min_sum}')





