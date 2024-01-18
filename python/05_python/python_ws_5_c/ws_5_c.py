def restructure_word(word, arr):
    for error in word:
        if error.isdecimal():
            for _ in range(int(error)):
                arr.pop()
        else:
            arr.remove(error)
    return arr
                
original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []
for i in original_word:
    arr.extend(i)
print(arr)

result = restructure_word(word, arr)
print(''.join(result))