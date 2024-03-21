import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    sdoku = [list(map(int,input().split())) for _ in range(9)]
    compared_list = list(range(1,10))
    cnt=1
    # 가로 검사
    for i in range(9):
        if sorted(sdoku[i]) != compared_list:
            cnt=0
            break

    # 세로 검사
    for i in range(9):
        col_arr =[]
        for j in range(9):
            if sdoku[j][i] not in col_arr:
                col_arr.append(sdoku[j][i])
        if sorted(col_arr) != compared_list:
            cnt=0
            break
    # 9등분하여 검사
    for col in range(0,9,3):
        for j in range(0,9,3):
            sdoku_arr = []
            for i in range(3):
                sdoku_arr.extend(sdoku[i+j][col:col+3])
            if sorted(sdoku_arr) != compared_list:
                cnt = 0
                break
    print(f'#{tc} {cnt}')
