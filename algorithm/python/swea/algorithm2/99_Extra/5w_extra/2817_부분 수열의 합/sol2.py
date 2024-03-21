import sys
sys.stdin = open('input.txt')

def subset_sum(start,result,K):
    global cnt
    if result == K:
        cnt +=1
        return

    for next in range(start,N):
        if result <= K:
            subset_sum(next+1, result+arr[next], K)

for tc in range(1,int(input())+1):
    N, K = map(int, input().split())
    arr = tuple(map(int, input().split()))
    cnt = 0
    subset_sum(0,0,K)
    print(f'#{tc} {cnt}')