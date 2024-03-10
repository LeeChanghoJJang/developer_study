# 1904 01타일 
import sys
sys.stdin = open('input.txt')

N=int(input())
DP = [1,2] + [0] * (N-2)
for i in range(2,N):
    DP[i] = (DP[i-1] + DP[i-2]) % 15746
print(DP[N-1])

