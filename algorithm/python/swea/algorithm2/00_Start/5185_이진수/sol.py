import sys
sys.stdin = open('input.txt')

hexs = []
bins = []

for i in range(16):
    bins.append(bin(i)[2:].zfill(4))
    hexs.append(hex(i)[2:].upper())
hex_to_bin = dict(zip(hexs,bins))

T = int(input())
# print(hex_to_bin)
for tc in range(1,T+1):
    N, number = input().split()
    result =''
    for i in number:
        result += hex_to_bin[i]
    print(f'#{tc} {result}')



