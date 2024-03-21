import sys
sys.stdin = open('input.txt')
T = int(input())
### Brute Force
def brute_force(pattern,target):
    # 둘다 첫 조사 시작지점 0번에서 시작
    pattern_index= 0
    target_index=0
    # 현재 조사위치가 조사대상의 범위를 벗어나기 전까지
    while target_index < len(target):
        # 일치하지 않으면
        if pattern[pattern_index] != target[target_index]:
            pattern_index -=1

        # 일치하면 => 사실상 항상
        target_index+=1
        pattern_index+=1

        # 패턴의 끝까지 index가 증가했다
        # 패턴의 끝까지 조사했다.
        if pattern_index == len(pattern):
            return True
    return False

# KMP 알고리즘
def KMP(pattern,target):
    def make_lps():
        # 내앞에 나와 동일한 패턴이 몇번 나왔는지
        lps = [0]*len(pattern)
        for idx in range(1,len(pattern)):
            if pattern[lps[idx-1]]==pattern[idx]:
                # 내 다음 조사 대상은, 내 위치 +1 번째부터 조사
                lps[idx] = lps[idx-1] + 1
        lps.insert(0,-1)
        return lps
    lps = make_lps()

    pattern_index = 0
    target_index = 0
    # 현재 조사위치가 조사대상의 범위를 벗어나기 전까지
    print(lps)
    while target_index < len(target):
        print(lps[pattern_index])
        print(target_index,target[target_index],pattern_index,pattern[pattern_index])
        # 일치하지 않으면
        if pattern[pattern_index] != target[target_index]:
            pattern_index = lps[pattern_index]

        # 일치하면 => 사실상 항상
        target_index += 1
        pattern_index += 1

        # 패턴의 끝까지 index가 증가했다
        # 패턴의 끝까지 조사했다.
        if pattern_index == len(pattern):
            return True
    return False
def boyer_moore(pattern,target):
    lps ={pattern[idx]: len(pattern) - 1 - idx for idx in range(len(pattern))} # 스킵 가능한 범위 기록
    print(lps)
    pattern_index = len(pattern)
    target_index = 0
    while target_index <=len(target) - pattern_index:
        for p_idx in range(pattern_index-1,-1,-1):
            if target[target_index+p_idx] != pattern[p_idx]:
                target_index += lps[target[target_index+p_idx]]
                target_index += lps.get(target[target_index+p_idx],len(pattern))
                break
    # rithm ---> m은 0 r은 4만큼 떨어짐


# 내 코드
for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    cnt=0
    boyer_moore(str1,str2)
    # print(KMP(str1,str2))
    for i in range(len(str2)-len(str1)+1):
        if str2[i:i+len(str1)] == str1:
            cnt = 1
            break
    print(f'#{tc} {cnt}')

