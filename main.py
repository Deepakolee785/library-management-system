#imporing modules
import display,detail,read_write,services
import sys
#main methid that runs program
def main():
    display.display()
    message = input("\t\tChoose Option: ")
    print()
    if message == '1':
        display.displayBook()
        main()
    elif message == '2':
        services.borrowBook()
        main()
    elif message == '3':
        services.returnBook()
        main()
    elif message == '4':
        print("\t\tExiting...\n")
        sys.exit()
    else:
        print("\t\tSorry! Invalid input.\n")
        ans  = input("\t\tDo you want to continue(y/n):")
        print()
        if ans == 'y':
            main()
        elif ans == 'n':
            print("\t\tExiting...\n")
            sys.exit()
        else:
            print("\t\tInvalid input.\nExiting...")
            sys.exit()       
#calling main function
main()
