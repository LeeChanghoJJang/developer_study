import sys
sys.stdin = open('input.txt')

n = int(input())

for i in range(n):
    # 찾고자 하는 문자열
    str1 = input()
    # 전체 문자열
    str2 = input()
    arr=[]
    # str1 문자중에서 str2에 가장 많은 문자를 뽑기 위해
    # str2에 str1의 문자열을 하나씩 뽑아서 반복문 순회
    for alpha in str1:
        cnt = str2.count(alpha)
        arr.append(cnt)
    print(f'#{i+1} {max(arr)}')