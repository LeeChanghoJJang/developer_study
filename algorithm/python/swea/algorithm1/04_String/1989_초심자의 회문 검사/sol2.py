import sys
sys.stdin = open('input.txt')

T = int(input())
# for문 이용해서 풀기
for tc in range(1,T+1):
    word = input()
    N = len(word)
    for i in range(N):
        if word[i] != word[N-1-i]:
            cnt=0
            break
    else:
        cnt = 1
    print(f'#{tc} {cnt}')