import sys
sys.stdin = open('sample.input.txt')

for tc in range(1,11):
    N = int(input())
    buildings = list(map(int,input().split()))
    cnt = 0
    for i in range(2,N-2):
        views = buildings[i-2:i+3]
        now = views.pop(2)
        max_view = max(views)
        if now > max_view:
           cnt += now - max_view
    print(f'#{tc} {cnt}')