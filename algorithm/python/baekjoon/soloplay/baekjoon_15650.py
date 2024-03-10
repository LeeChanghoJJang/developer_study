import sys
sys.stdin = open('input.txt')

# 부분집합을 구하는 방법으로 해봤으나 실패
N,M = map(int,input().split())
total_arr = list(range(N))
array=[]
def backtracking():
    if len(array) == M:
        print(' '.join(map(str, array)))
        return

    for i in range(1, N+1):
        if i not in array and (len(array)==0 or array[-1] < i):
            array.append(i)
            backtracking()
            array.pop()

backtracking()