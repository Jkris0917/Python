from contact_func import (
    show_contacts, add_contacts, update_contacts,
    search_contact, delete_contacts,
    load_contacts, save_contacts, save_logs
)

def main():
    contacts = load_contacts()
    print("== Contact Book ==")

    while True:
        print("\n[1] Show  [2] Add  [3] Update  [4] Search  [5] Delete  [6] Quit")
        choose = input("Choose: ")

        if not choose.isdigit():
            print("  Must be a number.")
            continue
        choose = int(choose)

        if choose == 1:
            show_contacts(contacts)

        elif choose == 2:
            name  = input("  Name: ").lower().strip()
            phone = input("  Phone: ").strip()
            email = input("  Email: ").strip()
            if not name:
                print("  Name cannot be blank.")
                continue
            add_contacts(contacts, name, phone, email)
            save_contacts(contacts)                        
            save_logs(f"Added: {name}")

        elif choose == 3:
            show_contacts(contacts)
            name  = input("  Name to update: ").lower().strip()
            if not name:
                print("  Name cannot be blank.")
                continue
            print("  (Press Enter to keep existing value)")
            phone = input("  New phone: ")
            email = input("  New email: ")
            update_contacts(contacts, name, phone, email)
            save_contacts(contacts)                        
            save_logs(f"Updated: {name}")

        elif choose == 4:
            name = input("  Search name: ").lower().strip()
            search_contact(contacts, name)

        elif choose == 5:
            name = input("  Delete name: ").lower().strip()
            delete_contacts(contacts, name)
            save_contacts(contacts)                        
            save_logs(f"Deleted: {name}")

        elif choose == 6:
            print("Goodbye!")
            break

main()