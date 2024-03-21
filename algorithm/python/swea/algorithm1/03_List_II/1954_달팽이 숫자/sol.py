import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 델타검색을 활용 (동,남,서,북)(cnt%4, cnt+=1)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    temp = [[0] * N for _ in range(N)]

    cnt = 0
    num_count = 1
    x = y = 0

    while num_count <= N ** 2:
        if x >= N or x < 0 or y < 0 or y >= N or temp[x][y] != 0:
            x -= dx[cnt % 4]
            y -= dy[cnt % 4]
            cnt += 1
            x += dx[cnt % 4]
            y += dy[cnt % 4]

        if temp[x][y] == 0:
            temp[x][y] += num_count
            x += dx[cnt % 4]
            y += dy[cnt % 4]
            num_count += 1

    print(f'#{tc}')
    for i in range(len(temp)):
        print(*temp[i])