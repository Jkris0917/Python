def show_contacts(contacts):
    """Show list of contacts"""
    if not contacts:
        print("No contacts yet")
    
    for name,info in contacts.items():
        print(f"\n{name.title()}")
        for field,value in info.items():
            print(f"{field}: {value}")
            
def add_contacts(contacts,name,phone,email):
    """Add a contacts"""
    contacts[name]= {"phone":phone,"email":email}
    print(f"'{name}' Added successfully!")