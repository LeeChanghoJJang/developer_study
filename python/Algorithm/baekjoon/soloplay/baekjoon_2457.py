import sys
sys.stdin = open('input.txt')
N= int(input())
princess = []
months = {0:0,1:31,2:59,3:90,4:120,5:151,6:181,7:212,8:243,9:273,10:304,11:334,12:365}
min_start_date = float('inf')
min_end_date= float('inf')
max_date = 0

def dates(month,day):
    return months[month-1] + day

flowers = sorted([list(map(int,input().split())) for _ in range(N)], key= lambda x:(x[0],x[1],x[2],x[3]))
while flowers:
    x1,y1,x2,y2 = flowers.pop(0)
    # 아무것도 없으면 넣자 솔직히
    if not princess:
        princess.append([x1,y1,x2,y2])

        min_start_date = min(min_start_date, dates(x1, y1))
        min_end_date = min(min_end_date, dates(x2, y2))
        max_date = max(max_date, dates(x2, y2))

    # 3월 이전일 때
    elif x1 < 3:
        # 시작날짜는 아무런 상관이 없으므로, 끝날짜만 보고 긴걸로 변경
        if max_date < dates(x2,y2):
            princess.pop()
            princess.append([x1,y1,x2,y2])

        min_start_date = min(min_start_date, dates(x1, y1))
        min_end_date = min(min_end_date, dates(x2, y2))
        max_date = max(max_date, dates(x2, y2))

    # 3월에서 11월 사이에 피는 경우
    elif 3 < x1 < 12:
        # 1,1, 6,30  5,15, 8,31
        # 교체조건 : princess가 고른 꽃 중 가장 이른 지는일짜인 min_date보다 시작이 적고, 지는일자가 max_date보다 긴경우
        if dates(princess[-1][0],princess[-1][1]) >= dates(x1,y1) or min_end_date >= dates(x1,y1) and max_date <= dates(x2,y2):
            princess.pop()
            princess.append([x1, y1, x2, y2])

        # 추가조건 : 지는날짜가 이전 지는 일자보다는 길어야함. 시작일자가 이전 지는 일자보다는 느려야함
        elif dates(x1,y1) <= max_date <= dates(x2,y2):
            princess.append([x1,y1,x2,y2])

        # 11월 이후에 진다면? (종료조건)
        if 334 <= dates(x2,y2):
            break

        min_start_date = min(min_start_date, dates(x1, y1))
        min_end_date = min(min_end_date, dates(x2, y2))
        max_date = max(max_date, dates(x2, y2))

    elif princess[0][0] >= 3:
        princess.clear()

print(princess)
