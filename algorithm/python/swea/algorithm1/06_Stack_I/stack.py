def push(n):
    global top
    top +=1
    if top ==size:
        print('overflow!')
    else:
        stack[top] = n

top = -1
size=10 
stack = [0]*size #최대 10개 push

top +=1
stack[top] = 10
top +=1
stack[top] = 20
push(30)

while top >= 0:
    top -=1
    print(stack[top+1])

def f2(n):
    n *= 2
    print(n)
    return

def f1(c,d):
    e = c + d
    f2(e)

a = 10
b = 20
c = a + b
f1(a, b)

## 재귀함수
def f(i,k):
    if i==k:
        return
    else:
        brr[i] =arr[i]
        f(i+1,k)
arr = [10,20,30]
N = len(arr)
brr = [0]* N

## memoization 활용
## 활용전
def fibo(n):
    global cnt
    cnt +=1
    if n<2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
cnt = 0
print(fibo(7),cnt)

## 활용 후
def fibo_memo(n):
    global cnt 
    cnt +=1 
    if n!=0 and memo[n]==0:
        memo[n] = fibo_memo(n-1) +fibo_memo(n-2)
    return memo[n]
cnt = 0
n=7
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1

