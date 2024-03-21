import sys
sys.stdin = open('input.txt')

def add(now):
    # now가 N보다 작음
    if now <= N:
        # 0이 아닌 경우에는 그 값을 반환
        if trees[now] != 0:
            return trees[now]
        # 만약 0이라면 더해줘야 겟쥬?
        elif trees[now] == 0:
            trees[now] = add(2 * now) + add(2 * now+1)
            return trees[now]
    # 초과 하는 경우는 0로 처리해서 TypeError 방지
    else:
        return 0

T = int(input())
for tc in range(1,T+1):
    N,M,L = map(int,input().split())
    trees = [0] * (N+1)
    for i in range(M):
        start,end = map(int,input().split())
        trees[start]= end
    print(f'#{tc} {add(L)}')