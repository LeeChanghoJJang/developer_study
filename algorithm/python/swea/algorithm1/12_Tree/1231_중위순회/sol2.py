import sys
import heapq
sys.stdin = open('input.txt')
def inorder(start):
    global result
    if start !=0:
        inorder(trees[start][0])
        result.append(values[start])
        inorder(trees[start][1])

for tc in range(1,11):
    N = int(input())
    trees = [[0,0] for _ in range(N+1)]
    values = [0]*(N+1)
    result = []
    for i in range(N):
        number, words, *digits = input().split()
        if digits:
            if len(digits) ==1:
                trees[int(number)][0] = int(digits[0])
            elif len(digits) == 2:
                trees[int(number)][0] = int(digits[0])
                trees[int(number)][1] = int(digits[1])
        values[int(number)] = words
    inorder(1)
    print(f'#{tc}',end=' ')
    print(*result,sep='')
