import sys
sys.stdin = open('input.txt')

# 첫번쨰 코드 36149KB, 7948ms
N,M = map(int,input().split())
temp = [input() for _ in range(N)]
cnt=0
for _ in range(M):
    a = input()
    for i in temp:
        if a==i:
            cnt+=1
            break
print(cnt)

# 두번째 코드 36552KB, 112ms
N,M = map(int,input().split())
temp = set()
cnt = 0
for _ in range(N):
    temp.add(input())

for i in range(M):
    if input() in temp:
        cnt+=1
print(cnt)
'''
코드리뷰
: for+if 쓰는거 보다 in + if을 쓰는게 훨씬 낫다.
'''