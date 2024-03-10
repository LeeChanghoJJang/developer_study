# 15649 N과 M (1)
import sys
sys.stdin = open('input.txt')
N, M = map(int,input().split())
total_arr = list(range(N))
array=[]

def backtracking():
    if len(array) == M:
        print(' '.join(map(str, array)))
        return

    for i in range(1, N+1):
        if i not in array:
            array.append(i)
            backtracking()
            array.pop()

backtracking()