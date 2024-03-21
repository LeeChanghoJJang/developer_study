import sys
sys.stdin = open('input.txt')

def operation(order, result):
    global plus, minus, product,divided,max_val,min_val
    if order == N:
        if result < min_val:
            min_val = result
        if result > max_val:
            max_val = result
        return
    else:
        if plus > 0:
            plus-=1
            operation(order+1,result + numbers[order])
            plus+=1
        if minus > 0:
            minus -= 1
            operation(order+1, result - numbers[order])
            minus += 1
        if product > 0:
            product -= 1
            operation(order+1, result * numbers[order])
            product += 1
        if divided > 0:
            divided -= 1
            operation(order+1, int(result / numbers[order]))
            divided +=1

for tc in range(1,int(input())+1):
    N = int(input())
    plus, minus, product, divided = map(int,input().split())
    numbers = list(map(int,input().split()))
    min_val = float('inf')
    max_val = float('-inf')
    operation(1,numbers[0])
    print(f'#{tc} {max_val-min_val}')
