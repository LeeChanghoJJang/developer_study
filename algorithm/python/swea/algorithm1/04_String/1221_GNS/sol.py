import sys
sys.stdin  = open('input.txt')
# 문자들의 순서를 딕셔너리로 정리
orders = {'ZRO':0,'ONE':1,"TWO":2,'THR':3,'FOR':4,'FIV':5,'SIX':6,'SVN':7,'EGT':8,'NIN':9}
# 테스트 케이스 수를 T로 받음
T = int(input())
for _ in range(1,T+1):
    # 테스트케이스 번호와 길이를 각 tc, length로 저장
    tc, length = input().split()
    # sort함수를 쓰기 위해 주어진 단어들을 language라는 변수에 리스트 형태로 저장
    language = input().split()
    print(f'{tc}')
    # language를 위에 정한 딕셔너리의 value값에 따라 정렬하기 위해,
    # sort의 기준을 orders에 x를 키값으로 넣은 value을 기준으로 정함
    language.sort(key=lambda x:orders[x])
    # language를 언팩하여 출력형태와 비슷하게 변형
    print(*language)