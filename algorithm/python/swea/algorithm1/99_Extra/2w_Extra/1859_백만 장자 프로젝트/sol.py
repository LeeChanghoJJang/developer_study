import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N= int(input())
    prices = list(map(int,input().split()))
    max_sum = 0
    while prices:
        max_val = max(prices)
        end_index = prices.index(max_val)
        max_sum += max_val * len(prices[:end_index]) - sum(prices[:end_index])
        if len(prices[end_index:]) !=0:
            prices = prices[end_index+1:]
    print(f'#{tc} {max_sum}')