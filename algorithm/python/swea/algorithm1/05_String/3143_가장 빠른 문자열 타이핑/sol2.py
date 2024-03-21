import sys
sys.stdin = open('input.txt')
T = int(input())

def brute_force(pattern,target):
    global cnt
    pattern_index = 0
    target_index = 0
    while target_index < len(target):
        if target[target_index] != pattern[pattern_index]:
            pattern_index = -1
        target_index += 1
        pattern_index += 1

        if pattern_index == len(pattern):
            pattern_index = -1
            cnt+=1
    return cnt
for tc in range(1,1+T):
    target, pattern = input().split()
    cnt = 0
    print(f'#{tc} {brute_force(pattern,target)}')