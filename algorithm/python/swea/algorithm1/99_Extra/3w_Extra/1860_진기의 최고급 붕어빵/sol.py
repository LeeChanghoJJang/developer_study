import sys
sys.stdin = open('input.txt')

T = int(input())
# 중복되서 기다리는 사람에 대한 고려 필요
for tc in range(1, T + 1):
    # N명에게 팔거이며, M초의 시간당 K개를 만듦
    N, M, K = map(int, input().split())
    # 시간대별로 사람들을 정렬시켜 순차적으로 받아가게 하자
    people = sorted(map(int, input().split()))
    # 초기 남은 빵 갯수는 처음 한사람 주고 남은 갯수
    bread = (people[0] // M) * K - 1  # 초기값에서 1 감소
    # 잔여시간만큼 다음 시간에 더해줄거임
    time = people[0] % M
    # 초기값 검사
    if bread < 0:
        possible = 'Impossible'
    else:
        possible = 'Possible'
        # 대기인원이 없을 때까지 진행
        for person in range(1, N):
            # 빵이 누적되는 건 좋지만, 짤린다. 기존 꺼에다가 추가하는 방식 필요
            produced_bread = ((people[person] - people[person - 1] + time) // M) * K
            bread += produced_bread
            bread -= 1  # 빵이 팔리면 1 감소
            time = (people[person] - people[person - 1] + time) % M
            if bread < 0:
                possible = 'Impossible'
                break
    print(f'#{tc} {possible}')




