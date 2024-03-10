books = ['홍길동전', '유연전', '심청전', '광문자전', '수성지']
authors = ['허균', '이항복', '작자 미상', '박지원', '임제']
for book_name, author_name in zip(books,authors):
    print(author_name,book_name,sep=' : ')
