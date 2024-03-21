import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    # 전체 색칠할 수 있는 공간 total_arr 정의
    total_arr = [[0]*10 for _ in range(10)]
    for _ in range(N):
        # 색칠을 시작하는 지점의 행과 열을 x1,y1
        # 색칠을 마무리하는 지점의 행과 열을 x2,y2
        # 칠하는 색깔을 color로 지정
        x1, y1, x2, y2, color = map(int, input().split())
        # 2차원 배열인 total_arr의 행과 열을 하나씩 순회
        # 단, 위에서 주어진 x1,y1 ~ x2,y2의 범위 내에서만 해당 컬러로 색칠
        for row in range(x1,x2+1):
            for col in range(y1,y2+1):
                total_arr[row][col] += color
        # 빨간색 : 1이고, 파란색 : 2임 --> 두개 합치면 보라색은 3이 됨
    result=0
    # 보라색이 2차원 배열 내에 어디 있는지 갯수를 세면 끝
    for row in range(10):
        result += total_arr[row].count(3)
    print(f'#{tc} {result}')