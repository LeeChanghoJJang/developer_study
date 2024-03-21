import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    min_val = float('inf')
    max_val = float('-inf')
    for number in map(int,input().split()):
        if number > max_val:
            max_val = number
        if number < min_val:
            min_val = number
    print(f'#{tc} {max_val - min_val}')