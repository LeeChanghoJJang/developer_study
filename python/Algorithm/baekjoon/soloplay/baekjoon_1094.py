# 1094번 막대기
# 임시리스트에 실제값을 추가하는 방법 
X = int(input())
temp =[]
bar=64
while sum(temp)<X:
  temp.append(bar)
  if sum(temp) == X:   
    break  
  elif sum(temp) > X:
    temp.pop()
  bar//=2
print(len(temp),temp,bar)
# 수정코드 
# X가 막대의 절반보다 큰 경우 그 때마다 막대를 추가(cnt+=1)
X = int(input())
# 64부터 1까지 막대의 길이 모든 경우를 모은 리스트
stick = [1<<(i-1) for i in range(7,0,-1)]
cnt =0 
for i in stick:
    # X가 막대의 길이보다 큰 경우, cnt를 늘리고 X에서 막대의길이를 차감한만큼 X 반환
    if X >= i:
       X -= i
       cnt += 1
    if X ==0: # X와 막대의길이가 같아지면 반복문 탈출
       break
print(cnt)
    