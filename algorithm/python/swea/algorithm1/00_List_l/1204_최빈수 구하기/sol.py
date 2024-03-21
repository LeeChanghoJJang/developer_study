import sys
sys.stdin = open('input.txt')
T = int(input())
for _ in range(1,T+1):
    tc = int(input())
    numbers = list(map(int,input().split()))
    count_arr = [0] * (max(numbers)+1)
    for i in numbers:
        count_arr[i] +=1
    max_val = 0
    max_index = 0
    for i in range(len(count_arr)):
        if count_arr[i] >= max_val:
            max_val = count_arr[i]
            max_index = i
    print(f'#{tc} {max_index}')