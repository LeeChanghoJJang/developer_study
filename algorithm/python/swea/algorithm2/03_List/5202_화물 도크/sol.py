import sys
sys.stdin = open('input.txt')
# 회의실 배정과 비슷한 문제임
for tc in range(1,int(input())+1):
    N= int(input())
    # 도크 사용신청들을 모아놓은 리스트(시작시간,완료시간)
    # 시작시간을 우선하여 오름차순하면서, 만약 종료시간이 뒤에 시작한 건이 더 짧을 때,
    # 쓸데없이 시간 축내는 신청건을 제외시키고, 종료시간이 더 가까운 것을 추가
    doc_time = sorted([list(map(int,input().split())) for _ in range(N)],key = lambda x:(x[0],x[1]))
    result =[]
    for i in range(N):
        # 기존 마지막 신청건의 종료시간이 새로 신청들어온 종료시간보다 느린 경우 교체
        if result and result[-1][1] > doc_time[i][1]:
            result.pop()
            result.append(doc_time[i])
        # 만일 신청건이 없거나, 기존 마지막 신청건의 종료시간보다 새로 신청 들어온 시작시간이
        # 느린경우에는 일단 추가
        elif not result or result[-1][1] <= doc_time[i][0]:
            result.append(doc_time[i])
    print(f'#{tc} {len(result)}')