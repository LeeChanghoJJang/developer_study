import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    # 전체페이지, A페이지, B 페이지
    P,Pa,Pb = map(int,input().split())
    temp = []
    # A페이지와 B페이지 2번 순회
    for page in [Pa,Pb]:
        # 페이지를 찾는 횟수를 카운트
        cnt = 1
        # 첫페이지
        start = 1
        # 전체 페이지
        end = P
        # 중간 페이지
        mid = (start + end) // 2
        if mid == page:
            temp.append(cnt)
            continue
        while mid != page:
            if page > mid:
                start = mid
            elif page <= mid:
                end = mid
            cnt += 1
            mid = (start+end)//2
        temp.append(cnt)
    if temp[0] > temp[1]:
        print(f'#{tc} B')
    elif temp[0] < temp[1]:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')