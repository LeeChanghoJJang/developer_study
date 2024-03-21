import sys
sys.stdin = open('input.txt')

def DFS(row,result,visited):
    global min_sum
    if row == N and result < min_sum:
        min_sum = result
        return
    elif result > min_sum:
        return

    for col in range(N):
        if col not in visited:
            visited.add(col)
            DFS(row+1,result + arr[row][col], visited)
            visited.remove(col)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 백트래킹 사용
    min_sum = float('inf')
    DFS(0,0,set())
    print(f'#{tc} {min_sum}')