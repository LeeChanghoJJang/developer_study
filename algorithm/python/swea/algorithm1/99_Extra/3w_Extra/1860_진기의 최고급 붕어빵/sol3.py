import sys
sys.stdin = open('input.txt')

T = int(input())
# 중복되서 기다리는 사람에 대한 고려 필요
for tc in range(1, T + 1):
    # N명에게 팔거이며, M초의 시간당 K개를 만듦
    N, M, K = map(int, input().split())
    # 시간대별로 사람들을 정렬시켜 내림차순으로
    people = sorted(map(int, input().split()),reverse=True)
    # 그 손님 전까지 누적된 빵이랄까..
    cumulated_bread = 1
    # 기본적으로 가능하다고 전제
    result = 'Possible'
    # 손님에게 다 팔때까지만 계속한다.
    while people:
        # 주문 받습니다. 끝에서부터요
        order = people.pop()
        # 생산가능여부 확인
        bread = order // M * K  - cumulated_bread
        if bread < 0:
            result = 'Impossible'
            break
        # 손님에게 한개 빵 팔때마다 누적판매량은 증가.
        cumulated_bread +=1
    print(f'#{tc} {result}')