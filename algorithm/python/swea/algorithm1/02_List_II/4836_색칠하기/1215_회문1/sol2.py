import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    N = int(input())
    palindrome = [input() for _ in range(8)]
    cnt = 0
    # 가로부터 검사
    for i in range(8):
        for j in range(9-N): # 0부터 4까지
            if palindrome[i][j:j+N] == palindrome[i][j:j+N][::-1]:
                cnt+=1

    # 세로부터 검사
    for col in range(8):
        for i in range(9-N):
            temp = []
            for row in range(i, N+i):
                temp += palindrome[row][col]
            if temp == temp[::-1]:
                cnt+=1

    print(f'#{tc} {cnt}')