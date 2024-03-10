import sys
from pprint import pprint
sys.stdin = open('input.txt')
arr = [list(map(int, input().split())) for _ in range(9)]
pprint(arr)
max_value = 0
max_row = 0
max_col = 0
for row in range(len(arr)):
    for col in range(len(arr[0])):
        if max_value <= arr[row][col]:
            max_value = arr[row][col]
            max_row = row
            max_col = col
print(max_value)
print(max_row+1, max_col+1)