import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    N = int(input())
    # 주어지 회문을 palindrome 에 저장
    palindrome = [input() for _ in range(8)]
    cnt = 0
    # 가로부터 검사
    for i in range(8):
        for j in range(9-N):
            # 가로로 해당하는 N의 길이만큼 문자열 인덱싱하여 한번에 회문검사
            if palindrome[i][j:j+N] == palindrome[i][j:j+N][::-1]:
                cnt+=1

    # 세로부터 검사
    for col in range(8):
        for i in range(9-N):
            # N의 길이에 해당하는 문자열을 담기 위한 임시 temp리스트
            temp = []
            for row in range(i, N+i):
                # 열 고정 행 우선순회로 temp에 문자열 하나씩 저장
                temp += palindrome[row][col]
            # N만큼 순회한후, temp에 다담기면 회문검사
            if temp == temp[::-1]:
                cnt+=1

    print(f'#{tc} {cnt}')