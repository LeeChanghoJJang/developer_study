import sys
sys.stdin = open('input.txt')

def binary(number):
    divided = 0.5
    result =''
    while number > 0 :
        if number >= divided:
            number -= divided
            result +='1'
        else:
            result +='0'
        divided /= 2
        if len(result) >= 13:
            return 'overflow'
    return result

T = int(input())
for tc in range(1,T+1):
    number = float(input())
    print(f'#{tc} {binary(number)}')