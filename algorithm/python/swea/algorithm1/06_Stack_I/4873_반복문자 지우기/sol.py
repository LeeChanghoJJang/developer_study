import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    word = input()
    temp = []
    for char in range(len(word)):
        if len(temp) != 0 and temp[-1] == word[char]:
            temp.pop()
        else:
            temp.append(word[char])
    print(f'#{tc} {len(temp)}')