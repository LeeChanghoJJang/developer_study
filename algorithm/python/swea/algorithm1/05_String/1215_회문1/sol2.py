import sys
sys.stdin = open('input.txt')

def is_palind(word):
    temp =''
    for i in range(len(word)-1,-1,-1):
        temp += word[i]
    # 새로 뒤집힌 문자와 원본이 같다면 회문
    return temp == word

for tc in range(1,11):
    N = int(input())
    data = [list(input()) for _ in range(8)]
    result = 0

    # 8열 or 8행을 모두 순회
    for i in range(8):
        # 그 중, 회문의 길이 N을 뺀 길이만큼 순회
        for j in range(8-N+1):
            temp_word_1 ='' # 가로 회문
            temp_word_2 ='' # 세로 회문
            for k in range(N):
                temp_word_1 += data[i][j+k]
                temp_word_2 += data[j+k][i]
            # 두 문자열에 대해 회문인지 판별
            if is_palind(temp_word_1):
                result +=1
            if is_palind(temp_word_2):
                result +=1

    print(f'#{tc} {result}')