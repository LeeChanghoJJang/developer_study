import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr= [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0
    for plus in range(N-M+1):
        for col in range(N-M+1):
            temp_sum = 0
            for row in range(M):
                temp_sum += sum(arr[row+plus][col:col+M])
            if max_sum < temp_sum:
                max_sum = temp_sum
    print(f'#{tc} {max_sum}')