import random,string,os,sys
#path of data file
if os.path.exists('books.txt'):
        path = "books.txt"
else:
        print("\n\t\t'books.txt' doesn't exist in the current directory.\n")
        sys.exit()
#return detail in list
def listBook():
        book_list = []
        books = open(path)
        for each_book in books:
            each_book = each_book.replace("\n",'').split(',')
            book_list.append(each_book)
        books.close()
        return book_list
#collects ids of book
def listOfBookIds():
        book_list1 = listBook()
        list_id = []
        for i in range(len(book_list1)):
            list_id.append(book_list1[i][0])
        return list_id
#returns book name from id
def bookName(e):
    book_list = listBook()
    idName = []
    for d in book_list:
        idName.append(d[:2])
    if e == 'b1':
        return (idName[0][1])
    elif e == 'b2':
        return (idName[1][1])
    elif e == 'b3':
        return (idName[2][1])
    elif e == 'b4':
        return (idName[3][1])
    elif e == 'b5':
        return (idName[4][1])
#returns book borrow price from id
def bookPrice(e):
    book_list = listBook()
    price = []
    for d in book_list:
        price.append(d[4])
    if e == 'b1':
        return (price[0])
    elif e == 'b2':
        return (price[1])
    elif e == 'b3':
        return (price[2])
    elif e == 'b4':
        return (price[3])
    elif e == 'b5':
        return (price[4])
#return book index from id
def returnBookIndex(b):
    if b == 'b1':
        x = 0
    elif b == 'b2':
        x = 1
    elif b == 'b3':
        x = 2
    elif b == 'b4':
        x = 3
    elif b == 'b5':
        x = 4
    return x
#unique code generator
def getCode(char = string.ascii_uppercase +string.digits +string.ascii_lowercase ):
    code = ''
    for x in range(4):
       code += ''.join(random.choice( char) )
    return code 
