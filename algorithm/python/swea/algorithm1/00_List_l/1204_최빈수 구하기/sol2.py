import sys
sys.stdin = open('input.txt')

for _ in range(1,int(input())+1):
    tc = int(input())
    students = list(map(int,input().split()))
    counting_arr = [0] * (max(students) + 1)
    for i in students:
        counting_arr[i] +=1
    max_val = 0
    max_witch = 0
    for i in range(1,len(counting_arr)):
        if max_val <= counting_arr[i]:
            max_val = counting_arr[i]
            max_witch = i
    print(f'#{tc} {max_witch}')