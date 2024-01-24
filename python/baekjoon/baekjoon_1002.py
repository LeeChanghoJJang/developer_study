# 1002번 터렛 (내 풀이)
import sys
N = int(input()) # 반복횟수를 N으로 설정
for _ in range(N):
    # 출발점의 좌표와 반지름을 x1,y1,r1 도착점은 x2,y2,r2
    x1,y1,r1,x2,y2,r2 = map(int,input().split()) 
    # 출발점과 도착점의 거리와 각 원의 반지름을 비교하여 교차점의 개수 구하기
    distance = (x2-x1)**2 + (y2-y1)**2
    if x1==x2 and y1==y2: 
        if r1==r2: # 동심원이면서 반지름이 같을 때
            print(-1)
        else: # 동심원이면서 반지름이 다를 때
            print(0)
    elif (r1+r2)**2 > distance: # 두 원의 반지름 합보다 두 지점의 거리가 작은 상황
        if (max(r1,r2) - min(r1,r2))**2 == distance:
            print(1) # 두 원이 내접할 때
        elif (max(r1,r2) - min(r1,r2))**2 > distance:
            print(0) # 큰 원이 작은 원을 포함하는 상황 
        else: # 큰 원과 작은 원이 교차하는 상황
            print(2)
    elif (r1+r2)**2 == distance: 
        print(1) # 두 원이 외접할 때
    else: # 두 원의 반지름의 합보다 두 지점의 거리가 작아 겹치는 상황
        print(0)

# 1002번 터렛 (코드 개선)
N = int(input()) # 반복횟수를 N으로 설정
for _ in range(N):
    # 출발점의 좌표와 반지름을 x1,y1,r1 도착점은 x2,y2,r2
    x1,y1,r1,x2,y2,r2 = map(int,input().split()) 
    # 출발점과 도착점의 거리를 distance로 정의
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5 
    if x1==x2 and y1==y2 and r1==r2: # 동심원이면서 반지름이 같을 때
        print(-1)
    elif abs(r1-r2) == distance and (r1+r2)== distance: # 두 원이 내접하거나 외접  
        print(1)  
    elif abs(r1-r2) < distance < (r1+r2): # 두 원이 두 점에서 교차할 때
        print(2)  
    else: # 동심원이면서 반지름이 다르거나 거리가 멀 때 
        print(0)
    
'''
코드리뷰
해결방법은 맞지만, if문이 중구난방으로 쓰여 여러번 읽어봐야 이해할 수 있다.
중첩되거나, 결과값이 같은 경우에는 되도록 하나로 묶어 코드를 간결하게 만들 필요 있음
'''