import sys
sys.stdin = open('input.txt')

def backtracking(start):
    food1, food2 = 0, 0
    global min_val
    if sum(visited) == N // 2:
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    food1 += foods[i][j] + foods[j][i]
                elif not visited[i] and not visited[j]:
                    food2 += foods[i][j] + foods[j][i]
        food1 //=2
        food2//=2
        if min_val > abs(food1 - food2):
            min_val = abs(food1 - food2)
            return

    for i in range(start, N):
        if not visited[i]:
            visited[i] = 1
            backtracking(i + 1)
            visited[i] = 0

T =int(input())
for tc in range(1,T+1):
    N = int(input())
    foods = [list(map(int,input().split())) for _ in range(N)]
    visited =[0] * (N+1)
    min_val = float('inf')
    backtracking(0)
    print(f'#{tc} {min_val}')