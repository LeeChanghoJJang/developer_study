def rental_book(name,number):
    print(f'남은 책의 수 : {decrease_book(3)}')
    return f'{name}님이 {number}권의 책을 대여하였습니다.'

number_of_book = 100

def decrease_book(number):
    global number_of_book
    return number_of_book - number

print(rental_book('홍길동',3))