import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1,T+1): # test_case 횟수만큼 반복
    # 배열의 총 길이 : N, 구간합의 길이 : M
    N,M =map(int,input().split())
    # 주어진 총 배열 : arr
    arr = list(map(int,input().split()))
    # 배열을 순회하기 위한 index i 설정
    i=0
    # while문을 반복하면서 구간합을 담을 temp 리스트 설정
    temp = []
    # while문을 순회하면서 구간합을 temp에 지속적으로 담음
    while i != N-M+1:
        temp.append(sum(arr[i:i+M]))
        i+=1
    # 모든 구간합을 담은 temp중 max값과 min값의 차이 출력
    print(f'#{test_case} {max(temp) - min(temp)}')