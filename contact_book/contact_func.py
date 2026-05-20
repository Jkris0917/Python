def show_contacts(contacts):
    """Show list of contacts"""
    if not contacts:
        print("No contacts yet")
        return
    
    for name,info in contacts.items():
        print(f"\n{name.title()}")
        for field,value in info.items():
            print(f"{field}: {value}")
            
def add_contacts(contacts,name,phone,email):
    """Add a contacts"""
    contacts[name]= {"phone":phone,"email":email}
    print(f"'{name}' added successfully!")
    
def update_contacts(contacts,name,phone,email):
    """Update a contact"""
    if name not in contacts:
        print(f"'{name}' not in the contact list")
        return
    
    if phone.strip() == '':
        contacts[name]["phone"] = phone

    if email.strip() == '':
        contacts[name]['email'] = email

    print(f"'{name}' updated successfully!")
    
def search_contact(contacts, name):
    """Search a contact"""
    if name not in contacts:
        print(f"'{name}' is not in contact list")
    else:
        print(name.title())
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    
def delete_contacts(contacts, name):
    if name not in contacts:
        print(f"'{name}' is not in contact list")
        return

    contacts.pop(name)
    print(f"'{name}' deleted successfully!")