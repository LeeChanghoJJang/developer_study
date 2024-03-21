import sys
sys.stdin = open('input.txt')
# 주어진 횟수만큼 숫자를 바꾸는 함수
def dfs(start,number_list):
    global result
    # number의 길이만큼 바꾸면
    if start == len(number_list):
        # 리스트 -> 문자열 -> 정수로 변환
        numbers = int(''.join(number_list))
        # 바뀐 숫자가 기존 result값보다 큰 경우 result값 갱신
        if result < numbers:
            result = numbers
        return
    # 성능 개선을 위해 ① 현재 몇번쨰 바꿨는지, ② 현재 바뀐 숫자를 묶어서 visited에 저장
    # 계속 함수를 호출하더라도, 기존에 visited에 있는 거면 바로 가지치기
    if (start, tuple(number)) in visited:
        return
    visited.add((start, tuple(number)))

    # 숫자 자리 교환
    for now in range(len(number_list)):
        for next in range(len(number_list)):
            number_list[now], number_list[next] = number_list[next], number_list[now]
            dfs(start+1,number)
            number_list[now], number_list[next] = number_list[next], number_list[now]

for tc in range(1,int(input())+1):
    number, cnt = input().split()
    number_list = list(number)
    cnt = int(cnt)
    visited = set()
    result =0
    dfs(0,number_list)
    print(f'#{tc} {result}')
