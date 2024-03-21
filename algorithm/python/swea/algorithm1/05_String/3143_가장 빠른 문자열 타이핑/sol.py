import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,1+T):
    A, unit = input().split()
    print(f'#{tc} {len(A)- (len(unit)-1) *A.count(unit)}')