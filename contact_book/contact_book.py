from contact_func import show_contacts,add_contacts,update_contacts,search_contact,delete_contacts

def main():
    contacts = {}
    print("==Contact Book==")
    
    
    while True:
        print("""[1] - Show All\n[2] - Add\n[3] - Update\n[4] - Search\n[5] - Delete\n[6] - Quit""")
        choose = input("Choose: ")
        if not choose.isdigit():
            print("Must be a number")
            continue
        choose = int(choose)
        
        if choose == 1:
            show_contacts(contacts)
            
        elif choose == 2:
            name = input("Enter Name: ").lower() 
            phone = input("Enter Phone: ")  
            email = input("Enter Email: ")
            add_contacts(contacts,name,phone,email)
            
        elif choose == 3:
            show_contacts(contacts)
            print("Select Name of Contact you want to update")
            try:
                name = input("Enter Name: ").lower()
                if name == '':
                    print('Provide name')
                phone = input("Enter Phone:")
                email = input("Enter Email: ")
                update_contacts(contacts,name,phone,email)
            except ValueError:
                print("Invalid!")
        
        elif choose == 4:
            name = input("Enter Name: ").lower()
            search_contact(contacts, name)
        
        elif choose == 5:
            name = input("Enter Name: ").lower()
            delete_contacts(contacts, name)
        
        elif choose == 6:
            print("Goodbye!")
            break
main()