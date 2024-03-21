import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    cnt=0
    palindrome_len = int(input())
    palindrome = [input() for _ in range(8)]

    # 가로검사
    for row in range(8):
        for col in range(8-palindrome_len+1):
            if palindrome[row][col:col+palindrome_len] == palindrome[row][col:col+palindrome_len][::-1]:
                cnt+=1
    # 세로검사
    for row in range(8):
        for plus in range(8-palindrome_len+1):
            string = ''
            for col in range(palindrome_len):
                string += palindrome[col+plus][row]
            if string == string[::-1]:
                cnt+=1

    print(f'#{tc} {cnt}')