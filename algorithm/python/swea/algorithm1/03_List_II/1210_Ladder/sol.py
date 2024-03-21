# 강사님 풀이
import sys
sys.stdin = open('input.txt')

# # 사다리의 크기 == 100 * 100
# def search(i,j):
#     # 방문 표시용 0으로 채워진 2차원 리스트
#     visited = [[0] * 100 for _ in range(100)]
#     # 출발시점의 j좌표 기록
#     original_j = j
#     while i != 99:  # 탐색 시작 -> i가 99가 될 때 까지
#         # 3방향 탐색  아래    왼     오
#         for dir in [(1, 0), (0, -1), (0, 1)]:
#             # 현재위치 i,j를 기준으로 dir[0],dir[1]
#             ni = i + dir[0]  # 다음 탐색 대상 i 좌표값
#             nj = j + dir[1]  # 다음 탐색 대상 j 좌표값
#             if 0 <= ni < 100 and 0 <= nj < 100 and arr[ni][nj] == 1:  # 이동 가능하다.
#                 if arr[ni][nj]==1:
#                     if not visited[ni][nj]:
#                         i, j = ni, nj
#                         visited[i][j] = 1
#                 if arr[ni][nj] == 2:
#                     return original_j
#
# for _ in range(1,11):
#     tc = int(input())
#     arr = [list(map(int,input().split())) for _ in range(100)]
#
#     # 최종 결괏값
#     result = 0
#     for j in range(100):
#         # 출발 지점 : i좌표 ==0으로 고정
#         if arr[0][j] ==1:
#             result = search(0,j)
#     print(result)


# 내코드
for test_case in range(1,11):
    N = int(input())
    # arr 리스트를 정의하여 행렬을 입력받음
    arr = [list(map(int, input().split())) for _ in range(100)]
    # x, y 초기좌표 위치 파악, start 정의
    x=99
    y=0
    for i in range(100):
        if arr[x][i]==2:
            y=i
            break
    # x는 99, y는 ?? 거꾸로 탐색
    # 위,왼,오
    dx = [-1,0,0]
    dy = [0,-1,1]
    way = 0
    while x != 0:
        for i in range(3):
            if x + dx[i] <0 or x + dx[i] >=100 or y+dy[i] < 0 or y+dy[i] >=100:
                continue
            if arr[x+dx[0]][y+dy[0]] ==0:
                continue
            if arr[x + dx[i]][y + dy[i]] and i !=way:
                way = i
                break
        # if 0 <= nx < 100 and 0 <= ny < 100:
        x += dx[way]
        y += dy[way]
    print(f'#{test_case} {y}')
