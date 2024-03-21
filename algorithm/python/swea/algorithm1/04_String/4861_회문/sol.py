import sys
sys.stdin = open('input.txt')

def Judge(N,M,palindrome):
    # 가로검사 : 가로는 전체 탐색
    result =''
    for row in range(N):
        # 열은 M길이만큼 조사하기 위해 시작인덱스를 N-M+1
        for col in range(N-M+1):
            if palindrome[row][col:col+M] ==palindrome[row][col:col+M][::-1]:
                result = palindrome[row][col:col+M]
                return ''.join(result)
    # 세로검사 : 세로는 열은 고정하고 행만 움직임
    for col in range(N):
        for start in range(N-M+1):
            # 전 구간 시작시 마다 M길이만큼 조사
            temp = []
            for row in range(M):
                temp.append(palindrome[row+start][col])
            if temp == temp[::-1]:
                result = temp
                return ''.join(result)

T = int(input())
for tc in range(1,T+1):
    # 길이가 M인 회문을 찾기 위함
    N,M = map(int,input().split())
    palindrome = [input() for _ in range(N)]
    print(f'#{tc} {Judge(N,M,palindrome)}')
