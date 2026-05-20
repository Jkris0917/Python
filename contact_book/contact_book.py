from contact_func import show_contacts,add_contacts

def main():
    contacts = {}
    print("==Contact Book==")
    print("""[1] - Show All\n[2] - Add\n[3] - Update\n[4] - Search\n[5] - Delete\n[6] - Quit""")
    
    while True:
        choose = input("Choose: ")
        if not choose.isdigit():
            print("Must be a number")
        choose = int(choose)
        
        if choose == 1:
            show_contacts(contacts)
            
        elif choose == 2:
            name = input("Enter Name: ")  
            phone = input("Enter Phone: ")  
            email = input("Enter Email: ")
            add_contacts(contacts,name,phone,email)
            
        elif choose == 3:
            pass
        
        elif choose == 4:
            pass
        
        elif choose == 5:
            pass
        
        elif choose == 6:
            print("Goodbye!")
            break
main()