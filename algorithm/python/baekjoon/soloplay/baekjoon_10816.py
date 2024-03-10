import sys
sys.stdin = open('input.txt')

N = int(input())
cards = sorted(map(int,input().split()))
M = int(input())
checks = map(int,input().split())
# 시간초과 뜰거임
# cnt=0
# for i in checks:
#     cnt=0
#     for j in cards:
#         if i==j:
#             cnt+=1
#     print(cnt,end=' ')

temp = []
print(cards)
for check in checks:
    cnt = 0
    start = 0
    end = N
    while start < end:
        mid = (start + end) // 2
        if cards[mid] <= check:
            start = mid + 1
        elif cards[mid] >= check:
            end = mid - 1
        if cards[mid] == check:
            cnt+=1

        print(start,end,mid,check)
    temp.append(cnt)
print(temp)

# print(binarySearch(cards,checks))


