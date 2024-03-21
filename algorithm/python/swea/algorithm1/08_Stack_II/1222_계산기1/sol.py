import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    N = int(input())
    num_list = map(int,input().split('+'))
    print(f'#{tc} {sum(num_list)}')