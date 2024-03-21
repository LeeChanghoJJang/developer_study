import sys
sys.stdin = open('input.txt')

for tc in range(1,int(input())+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(1 << N):
        result = []
        for j in range(N):
            if i&(1<<j):
                result.append(arr[j])
        if sum(result) == K:
            cnt+=1
    print(f'#{tc} {cnt}')