# 1024번 수열의합
# 내가 제출한 최초 코드(시간초과)
import sys
N,L = map(int,input().split())

def arr_find(N,L):
    # 시간초과를 줄이기 위해 N이 L로 나뉘거나, L의 길이가 너무 긴 경우 제외
    if N//L ==N/L or 2*N/L==(2*N)//L or N//L > L//2:
      i=0
      while sum(range(L+i)) <= N:
        # 총합에서 연속된 숫자 갯수의 합계와 비교하기 위해 그 차이가 갯수만큼 나뉘어진다는 것 이용  
        if (N - sum(range(L+i)))%(L+i)==0 and len(range(L+i))<=100:
            plus = (N - sum(range(L+i)))//(L+i)
            print(*range(plus,L+i+plus))
            break
        i+=1
      else:
          print(-1)
    else:
        print(-1)    
arr_find(N,L)

# 수정된 코드 
N, L = map(int, input().split())
# N = (x+1) + .... (x+n) = nx + n(n-1)/2  => x= N/n -(n-1)/2  => 역산
for n in range(L, 101):
    x = N/n - (n+1)/2
    # x는 정수여야 하므로, 
    if int(x) == x:
        x = int(x)
        if x + 1 >= 0:
            for i in range(x+1, x+n+1):
                print(i, end=" ")
            break
else:
    print(-1)