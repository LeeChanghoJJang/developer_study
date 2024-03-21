import sys
sys.stdin = open('input.txt')

def carts(now,max_val):
    global result
    if max_val > result:
        return

    if all(visited):
        max_val += battery[now][0]
        if result > max_val:
            result = max_val
    else:
        for next in range(1,N):
            if not visited[next] and now != next:
                visited[next] = 1
                carts(next,max_val+battery[now][next])
                visited[next] = 0
    return result

T = int(input())
for tc in range(1,T+1):
    N =int(input())
    battery = [list(map(int,input().split())) for _ in range(N)]
    visited = [0] * N
    visited[0] = 1
    result = N *101
    result = carts(0,0)
    print(f'#{tc} {result}')