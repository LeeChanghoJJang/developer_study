import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    N, password = input().split()
    password = list(password)
    temp = []
    for i in password:
        if len(temp) !=0 and temp[-1] == i:
            temp.pop()
        else:
            temp.append(i)
    print(f'#{tc} {"".join(temp)}')