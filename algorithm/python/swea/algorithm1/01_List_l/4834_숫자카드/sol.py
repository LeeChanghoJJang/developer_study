import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    # 카드 총 숫자 나열
    cards = int(input())
    # 카드의 장수를 가산하기 위한 count 행렬 정의
    count_arr = [0]*10
    # 가장 많은 장수를 반환해야 하므로 max_number 정의
    max_number =0
    # 가장 큰 숫자를 반환해야 하므로 max_index 정의
    max_index=0
    # 카드의 숫자가 0가 될때까지 각 1자리씩 추출
    while cards:
        # 카드를 10으로 나눈 몫을 share, 나머지를 rest로 함
        share, rest = divmod(cards, 10)
        # 십진수이므로 rest가 숫자카드 하나 임
        # rest가 나올때마다 카운트 행렬에 해당되는 인덱스에 값을 1씩 가산
        count_arr[rest] += 1
        # cards는 share로 갱신
        cards = share
    # 카운트행렬은 완성
    # 가장 큰 숫자 max_number와 max_index를 찾아야 함
    # enumerate을 이용해 카운트행렬에서 가장 큰값과 그 인덱스를 구하여 결과값 반환
    for index, number in enumerate(count_arr):
        # 카드 장수가 카운트행렬에서 가장 많은 값과 같을 경우
        if number == max(count_arr):
            # 인덱스가 가장 많은 장수 중 가장 큰 수가 됨
            # 작은것부터 순회하기 때문에 같은 장수면 가장 큰수가 인덱스에 저장됨
            max_index = index
            max_number = number
    print(f'#{test_case} {max_index} {max_number}')