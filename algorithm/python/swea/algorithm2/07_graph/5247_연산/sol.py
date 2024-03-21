import sys
sys.stdin = open('input.txt')
# 런타임오류 존나 뜸
def BFS(N,M):
    j = 0
    temp = {N}
    result = 0
    if N > M:
        result = (N - M) // 10
        temp = {N - (N - M) // 10 * 10}
    while j <= int(1e6):
        temp_set = set()
        j += 1
        for i in temp:
            if not (0 < i < 2 * max(M + 1, N + 1, int(1e6))):
                continue
            for next in [i - 1, i + 1, i * 2, i - 10]:
                if next == M:
                    result += j
                    return result
                elif 0 < next <= int(1e6):
                    temp_set.add(next)
            temp = temp_set
for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    print(f'#{tc} {BFS(N,M)}')

