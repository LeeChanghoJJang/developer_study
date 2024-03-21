import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    # 모든 부분집합 구하기
    result=[]
    # 1부터 12의 부분집합을 구하므로 모든 부분집합의 개수 1<<12에서 반복문 순회
    for i in range(1<<12):
        temp=[]
        # 각 i의 이진수에 1이 해당하는 위치만 temp에 가산(부분집합 원소 추가)
        for j in range(12):
            if i&(1<<j):
                temp.append(j+1)
        # temp가 다채워지면(부분집합 하나 완성되면) 합, 길이조건 비교
        if sum(temp) ==K and len(temp)==N:
            # 충족하는 애들만 result에 추가
            result.append(temp)
    print(f'#{tc} {len(result)}')