# 1016번 제곱ㄴㄴ수
# 첫번째 풀이(시간초과로 실패)
min_num, max_num = map(int,input().split()) 
len_max_min = max_num - min_num +1 # min부터 max까지의 길이

temp =[] 
for i in range(2,int(max_num**0.5)+1): # 2에서 max_num의 제곱근 값까지 순회
  # 제곱수로 나누어지는 수를 min~max 사이에서 도출하여 temp 리스트에 합산
  temp.extend(list(filter(lambda x:x%(i**2)==0,range(min_num,max_num+1))))
print(len_max_min - len(set(temp))) # 전체에서 제곱수로 나누어지는 경우를 전부 차감 

# 두번째 풀이(시간초과)
import sys
min_num, max_num = map(int,sys.stdin.readline().split())
len_max_min = max_num - min_num +1
# max길이만큼 행렬 생성하고, min전까지는 False처리 
num = [False] * min_num + [True] * (max_num-min_num+1) 
if min_num <2:
    min_num =2
# min~ max값까지 순회
for i in range(min_num,max_num+1):
    # 2부터 max_num의 제곱근까지 순회
    for j in range(2,int(max_num**0.5)+1):
        # 제곱수로 나누어지는 경우는 num행렬에서 0으로 변경
        if i>j and i%(j**2)==0: 
            num[i] = False
print(sum(num))

# 세번째 풀이(메모리 초과 : 에라토스테네스의 체)
min_num, max_num = map(int,input().split())
arr = [0] + [1] * (max_num) # max길이만큼 행렬 생성하고, min전까지는 False처리 

for i in range(2,int(max_num**0.5)+1):
  # 중복을 최대한 막기 위해, 제곱근을 한번 탐색한 경우는 제외하기 위해 
  # 값이 0인 경우에는 continue 
  if arr[i]==0:
    continue
  for j in range(i*i,max_num+1,i*i): # 제곱수마다 값을 0로 변경 
    arr[j]=0
print(sum(arr[min_num:]))

# 네번째 풀이(통과)
min, max = map(int, input().split())
answer = max - min + 1
divisible = [False] * (max-min+1)

for i in range(2, int(max**0.5+1)):
    square = i**2
    for j in range((((min-1)//square)+1)*square, max+1, square):
        if not divisible[j-min] :
            divisible[j-min] = True
            answer -= 1
print(answer)
