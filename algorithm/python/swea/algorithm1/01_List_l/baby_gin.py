'''
0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를 갖는 경우를 
run이라고 하고, 3장의 카드가 동일한 번호를 갖는 경우를 triplet이라고 한다.

그리고 6장의 카드가 run과 triplet로만 구성된 경우를 baby-gin으로 부른다
667767은 두 개의 triplet 이므로 baby-gin이다(666,777)
054060은 한 개의 run과 한 개의 triplet이므로 역시 baby-gin이다.(456,000)
101123은 한 개의 triplet이 존재하나, 023이 run이 아니므로 baby-gin이 아니다


counts 배열을 만든다 
예시 1 : 444345
counts = [0,0,1,4,1,0,0,0,0,0] K = 10이라고 가정
run 조사 후 run 데이터 완전 삭제
counts = [0,0,0,3,0,0,0,0,0,0] baby-gin!

triplet 조사 후 tripelt 데이터 완전 삭제
counts = [0,0,1,1,1,0,0,0,0,0] baby-gin!
'''

num =456789 # Baby Gin 확인할 6자리 수
c = [0] * 12 # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트
for i in range(6):
    c[num%10] +=1
    num //=10

i=0
tri = run = 0
while i<10:
    if c[i] >=3:
        c[i] -=3
        tri +=1
        continue
    if c[i] >=1 and c[i+1]>=1 and c[i+2] >=1: # run 조사 후 데이터 삭제
        c[i]-=1
        c[i+1]-=1
        c[i+2]-=1
        run +=1
        continue
    i+=1
if run +tri ==2:
    print("Baby Gin")
else:
    print("Lose")

