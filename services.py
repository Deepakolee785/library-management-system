#import modules
import detail,display,read_write
import sys,datetime,random
#function for borrowing
def borrowBook():
    id_list = detail.listOfBookIds()
    book_list = detail.listBook()
    #borrowing process
    borrow_another = True
    total_price = 0
    total_books_borrowed = ""
    borrowed_book_index = []
    borrowed_book_id = []
    #multiple book borrowing
    while borrow_another:
        book_id = input("\t\tEnter the book id:").lower()
        print()
        if book_id in id_list:
            book_index = id_list.index(book_id)
            borrowed_book_index.append(book_index)
            borrowed_book_id.append(book_id)
            #getting details of borrowed book
            borrowed_book = book_list[book_index][1]
            price = float(book_list[book_index][4].replace('$',""))
            total_price += price
            total_books_borrowed += str(borrowed_book+';')
            borrow_again = input("\t\tDo you want to borrow another book(y/n):")
            print()
            if borrow_again == 'y':
                borrow_another = True
            else:
                borrow_another = False
        #if user give invalid id of book
        else:
                print("\t\tWe don't have book with this ID.Please enter valid id listed in table.")
                print()
                m = input("\t\tDo you want to continue(y/n):").lower()
                print()
                if m == 'y':
                    borrowBook()
                else:
                    #exits function
                    return None       
    name = input("\t\tEnter your name:").lower()
    print()
    date = str(datetime.date.today().strftime("%Y-%m-%d"))
    time = str(datetime.datetime.today().strftime("%H:%M"))
    dr = (datetime.datetime.today()+datetime.timedelta(days=10)).strftime("%Y-%m-%d")
    borrow_code = detail.getCode()
    #display bill of borrow
    display.displayInvoice(name,date,time,borrowed_book_id,total_price,dr)
    ans = input("\t\tDo you want to pay the amount(y/n):")
    print()
    if ans == 'y':
        file_name = "borrower/invoice/"+name+'_'+borrow_code+'_'+date+".txt"
        #create a file for each borrow with different name
        read_write.makeBorrowedFile(file_name,name,date,time,borrowed_book_id,total_price)
        #saves all borrowed log
        f1 = open("borrower/main_borrower.txt",'a')
        for m in borrowed_book_id:
            f1.write(str(name+","))
            f1.write(str(m+","))
            f1.write(str(date+","))
            f1.write(str(borrow_code+"\n"))
        f1.close()
        #updates qty of book in each borrow
        read_write.decreaseQuantity(borrowed_book_index)
        print("\t\tThank you!",name," for borrowing from us!")
        print("\n\t================================================\n\n")         

#function for returning 
def returnBook():
    name = input("\t\tEnter your name:").lower()
    print()
    borrower_detail = []
    borrower_name = []
    all_borrowed_book =[]
    f = open("borrower/main_borrower.txt")
    for i in f:
        if name in i:
            a = i.replace("\n",'').split(",")
            b = a[1]
            all_borrowed_book.append(b)
        i = i.replace("\n",'').split(",")
        borrower_detail.append(i)
    f.close()
    for j in borrower_detail:
        j[1] = j[1].replace(";"," ").split()
        borrower_name.append(j[0])
    #returning process
    if name in borrower_name:
        borrower_index = borrower_name.index(name)
        borrowed_book = []

        date = str(datetime.datetime.now().strftime("%Y-%m-%d"))
        time = str(datetime.datetime.now().strftime("%H:%M"))

        #display borrowed books
        display.displayBookReturning(name,all_borrowed_book)


        return_book_id = input("\t\tEnter id of  book you want to return: ")
        print()
        f3 = open("borrower/main_borrower.txt")
        for each_line in f3:
            if name and return_book_id in each_line:
                each_line = each_line.replace("\n",'').split(',')
                z = each_line[1]
                borrowed_book.append(z)
        f3.close()
        #fine calculation
        date_list = []
        for x in borrower_detail:
            date_list.append(x[2])
        borrow_code = borrower_detail[borrower_index][3]
        da = date_list[borrower_index]
        db = datetime.datetime.strptime(da,"%Y-%m-%d")
        dr = datetime.datetime.now()
        d=(dr-db).days
        fine = (d*10)/100
        if d>10:
            f = fine
            print("\t\tMr."+name+",you are "+str(d)+" days late.\n\t\tYou have to pay $"+str(fine)+" as fine.\n")
        else:
            f = 0
        #create log for each return   
        n = "returns/"+name+"_"+str(date)+".txt"
        read_write.makeReturnFile(n,name,date,time,borrowed_book,borrower_index,da,f)
        returned_book_index = []
        for m in borrowed_book:
            returned_book_index.append(detail.returnBookIndex(m))   
        #updates qty of book in each return
        read_write.increaseQuantity(returned_book_index)
        #deletes borrowed file and main log of borrower
        fn = "borrower/invoice/"+name+'_'+borrow_code+'_'+da+".txt"
        read_write.deleteBorrower(fn,borrow_code,return_book_id)
        print("\t\tSuccessfully returned.\n\n")
        print("\n\t================================================\n\n")
        ans = input("\t\tDo you want to continue returning(y/n):")
        print()
        if ans == 'y':
            returnBook()    
    else:
        print("\n\t\tSorry "+name+"!,your name is not found in borrower list.\n\t\tPlease check spelling and enter again.\n")
        ans = input("\t\tDo you want to continue reurning(y/n):")
        print()
        if ans == 'y':
            returnBook()
