# 아래 함수를 수정하시오.
def count_character(obj,char2):
    cnt=0
    for i in obj:
        if i== char2:
            cnt+=1
    return cnt
    
result = count_character("Hello, World!", "o")
print(result)  # 2
