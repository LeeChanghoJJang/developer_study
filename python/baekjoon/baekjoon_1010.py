# 1010번 다리 놓기(최초 풀이)
import sys
T = int(sys.stdin.readline()) # 입력횟수 
for tc in range(T):
  # 왼쪽 사이트 :N개, 오른쪽 사이트 : M개
  N, M = map(int,sys.stdin.readline().split()) 
  # 이 문제는 조합문제로, 오른쪽 사이트 갯수 중, 왼쪽 사이트 갯수만큼 순서없이 선택
  temp_sum, divided_sum  = 1,1
  for i in range(1,N+1): 
    temp_sum *= M+1-i
    divided_sum*=i
  print(temp_sum//divided_sum)

# 1010번 다리 놓기(개선된 코드)
import sys
T = int(sys.stdin.readline()) # 입력횟수

def factorial(n): # 같은 코드를 재사용하기 위해 함수 정의
    num=1
    for i in range(1,n+1):
        num*=i
    return num

for tc in range(T):
  # 왼쪽 사이트 :N개, 오른쪽 사이트 : M개
  N, M = map(int,sys.stdin.readline().split()) 
  print(factorial(M) // (factorial(N)*factorial(M-N)))
  '''
  코드 리뷰
  팩토리얼이 자주 사용되므로 math 라이브러리를 사용하거나,
  factorial 함수를 정의하면 코드를 간결하게 나타낼 수 있었음
  '''