# python_ws_5_4.py

# def capitalize_words(text):
#     words = text.split()
#     capitalized_words = [word.capitalize() for word in words]
#     return " ".join(capitalized_words)

# result = capitalize_words("hello, world!")
# print(result)
def capitalize_words(text):
    words =[]
    for alpha in range(len(text)):
        if alpha==0 and text[alpha].isalpha():
            words.append(text[alpha].upper())
        elif text[alpha-1]==' ' and text[alpha].isalpha():
            words.append(text[alpha].upper())
        else:
            words.append(text[alpha])
    return ''.join(words)

result = capitalize_words("hello, world!")
print(result)