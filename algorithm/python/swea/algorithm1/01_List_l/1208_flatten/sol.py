import sys
sys.stdin = open('input.txt')

T = 10
for test_case in range(1, T + 1):
    cnt = int(input())
    dump = list(map(int,input().split()))
    # 해당 dump의 max,min값을 담을 변수
    cul_sum_max = 0
    cul_sum_min = 0
    # 해당 dump의 max,min값의 누적값을 담을 변수
    result_max = 0
    result_min = 0
    # 현재상태의 max와 min값 설정
    max_value = max(dump)
    min_value = min(dump)
    while result_max <= cnt:
        # max값의 count를 cul_sum에 누적
        cul_sum_max += dump.count(max_value)
        # cul_sum에 누적된 count를 result_max값에 누적
        result_max += cul_sum_max
        # max_value의 높이를 다 퍼내고 -1처리
        max_value -=1
    while result_min <= cnt:
        # min값의 count를 cul_sum에 누적
        cul_sum_min += dump.count(min_value)
        # cul_sum에 누적된 count를 result_min값에 누적
        result_min += cul_sum_min
        # min_value의 높이를 다 쌓고 +1처리
        min_value +=1
    # 횟수를 초과하여 쌓거나 퍼낸 경우, 각각 이전숫자로 조정
    if result_min > cnt:
        min_value -=1
    if result_max > cnt:
        max_value +=1
    print(f'#{test_case} {max_value- min_value}')