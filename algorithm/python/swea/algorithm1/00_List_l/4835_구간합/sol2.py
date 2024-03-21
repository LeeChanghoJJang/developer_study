import sys
sys.stdin = open('sample_input.txt')

T  = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    max_val = float('-inf')
    min_val = float('inf')
    for i in range(N-M+1):
        if max_val < sum(arr[i:i+M]):
            max_val = sum(arr[i:i+M])
        if min_val > sum(arr[i:i+M]):
            min_val = sum(arr[i:i+M])
    print(f'#{tc} {max_val - min_val}')