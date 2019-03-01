import detail
import os
#make borrowed log
def makeBorrowedFile(file_name,name,date,time,borrowed_book_id,total_price):
    f = open(file_name,'w')
    f.write("\t\t\tElectronic invoice\n\t\t\t===================\n\n")
    f.write(str("\t\tName:"+name+"  Date:"+date+"  Time:"+time+"\n"))
    f.write(str("\t\t_________________________________________________________\n"))
    f.write(str("\t\tS.N.\tName of Book\t\tQuntity\t\tprice\n"))
    f.write(str("\t\t_________________________________________________________\n"))
    h = 1
    for g in borrowed_book_id:
        f.write(str(" \t\t"+str(h)+'.'+'\t'+str(detail.bookName(g))+" \t\t1\t\t"+str(detail.bookPrice(g))+"\n"))
        h+=1
    f.write(str("\t\t----------------------------------------------------------\n\t\t\t\t\t\tTotal:$"+str(total_price)+"\n"))
    f.close()
#decreases qty by 1
def decreaseQuantity(borrowed_book_index):
    book_list = detail.listBook()
    f2 = open(detail.path,'w')
    for index in borrowed_book_index:
        a = int(book_list[index][3])
        b = str(a-1)
        book_list[index][3] = book_list[index][3].replace(str(a),b)
    for each in book_list:
        each = ','.join(each)
        f2.write(str(each+"\n"))
    f2.close()
#make returned log
def makeReturnFile(file,name,date,time,borrowed_book,borrower_index,da,f):
    file = open(file,'w')
    file.write("\t\t\tElectronic invoice\n\t\t\t===================\n\n")
    file.write(str("\t\tName:"+name+"  Date:"+date+"  Time:"+time+"\n"))
    file.write(str("\t\t______________________________________________________\n"))
    file.write(str("\t\tS.N.\tName of Book\t\tQuntity\n"))
    file.write(str("\t\t______________________________________________________\n"))
    c = 1
    for g in borrowed_book:
        file.write(str(" \t\t"+str(c)+'.'+'\t'+str(detail.bookName(g))+" \t\t1\t\n"))
        c +=1
    file.write(str("\t\t------------------------------------------------------\n\t\tBorrowed Date:"+da+"\t\tLate Fine:$"+str(f)+"\n"))
    file.close()   
#increases qty by 1
def increaseQuantity(returned_book_index):
    book_list2 = detail.listBook() 
    f2 = open(detail.path,'w')
    for index in returned_book_index:
        a = int(book_list2[index][3])
        b = str(a+1)
        book_list2[index][3] = book_list2[index][3].replace(str(a),b)
    for each in book_list2:
        each = ','.join(each)
        f2.write(str(each+"\n"))
    f2.close()
#delete all info of borrow after returning books  
def deleteBorrower(borrower_file_name,borrow_code,return_book_id):
    #deletes borrowed log file
    try:
        os.remove(borrower_file_name)
    except:
        pass
    #deletes form main log of borrower
    e=''
    file = open("borrower/main_borrower.txt")
    for each_borrower in file:
        if borrow_code and return_book_id  not in each_borrower:
            e += each_borrower
    file.close()
    file1 = open("borrower/main_borrower.txt",'w')
    file1.write(e)
    file1.close()       
