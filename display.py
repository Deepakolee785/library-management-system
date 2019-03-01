import detail
#first display text
def display():
    print("\t        _______________________________________\n")
    print("  \t\t          Library Management System")
    print("\t        _______________________________________\n")
    print("\t\t\t1.Display Book\n\t\t\t2.Borrow Book\n\t\t\t3.Return Book\n\t\t\t4.Exit")
    print("\t        _______________________________________\n")
#book information
def displayBook():
    b_list = detail.listBook()
    print(" \n\n=====================================================")
    print("\n\t\t\tBook Information")
    print("\t\t        -----------------------------")

    print("    ______________________________________________________________")
    print("\tBook Id","Book Name","Author's Name","Quantity","   "+"Price",sep=" \t")
    print("    ______________________________________________________________")
    for m in range(len(b_list)):
            print("   \t"+b_list[m][0],b_list[m][1],b_list[m][2],"    "+b_list[m][3],"   "+b_list[m][4],sep="\t")
    print("    ______________________________________________________________")
    
    print()
    print(" ======================================================\n\n")
#borrowing bill
def displayInvoice(name,date,time,book_id,total_price,return_date):
    print("\n\t===========================================")
    print("\n\t\t\tElectronic Invoice\n\t\t---------------------------------------------------")
    print("\t\tName-"+name+"  Date-"+date+"  Time-"+time)    
    print("\t\t____________________________________")
    print("\t\tS.N.\tName of Book\tQuntity\tprice")
    print("\t\t____________________________________")
    h = 1
    for g in book_id:
        print(" \t\t"+str(h)+'.'+'\t'+detail.bookName(g)+" \t1\t"+detail.bookPrice(g))
        h+=1
    print("\t\t---------------------------------------------------\n\t\t\t\t\t\tTotal:$",total_price)
    print("\t\t____________________________________\n\t\tNote:The return date is:"+str(return_date))
    print("\t\t10 cents will be charged per book per each day.\n\t\t____________________________________\n")
    print()
    print("\t===========================================\n")
#books borrowed by user
def displayBookReturning(name,borrowed_book):
    h = 1
    print("\t\tBooks borrowed by you Mr."+name+" are:")
    print("\t\t____________________________________")
    print()
    for g in borrowed_book:
        print("\t\t"+str(h)+'.'+str(detail.bookName(g))+"\t"+str(g))
        h+=1
    print("\t\t____________________________________\n")
