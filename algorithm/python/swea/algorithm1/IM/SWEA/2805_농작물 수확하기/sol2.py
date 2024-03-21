import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    result = 0

    # 상반구와 하반구를 나누어 합산
    for row in range(N//2+1):
        if row ==N//2:
            result += sum(arr[row])
        else:
            mid = N // 2
            result += sum(arr[row][mid - row : mid + row + 1])  # 상반구
            result += sum(arr[N-1-row][mid - row : mid + row + 1])  # 하반구

    print(f'#{tc} {result}')