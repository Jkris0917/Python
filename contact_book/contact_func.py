import json
from datetime import datetime

FILENAME = "contact_book/contacts.json"
LOGS = "contact_book/logs.txt"

def show_contacts(contacts):
    """Show all contacts."""
    if not contacts:
        print("  No contacts yet.")
        return
    for name, info in contacts.items():
        print(f"\n  {name.title()}")
        for field, value in info.items():
            print(f"    {field}: {value}")

def add_contacts(contacts, name, phone, email):
    """Add a new contact."""
    contacts[name] = {"phone": phone, "email": email}
    print(f"  '{name.title()}' added successfully!")

def update_contacts(contacts, name, phone, email):
    """Update phone/email — blank input keeps existing value."""
    if name not in contacts:
        print(f"  '{name}' not found.")
        return
    if phone.strip() != '':
        contacts[name]["phone"] = phone
    if email.strip() != '':
        contacts[name]["email"] = email
    print(f"  '{name.title()}' updated successfully!")

def search_contact(contacts, name):
    """Search contact by name."""
    if name not in contacts:
        print(f"  '{name}' not found.")
        return
    print(f"\n  {name.title()}")
    print(f"    Phone: {contacts[name]['phone']}")
    print(f"    Email: {contacts[name]['email']}")

def delete_contacts(contacts, name):
    """Delete a contact."""
    if name not in contacts:
        print(f"  '{name}' not found.")
        return
    contacts.pop(name)
    print(f"  '{name.title()}' deleted successfully!")

def save_contacts(contacts):          
    """Save contacts dict to JSON file."""
    with open(FILENAME, "w") as f:
        json.dump(contacts, f, indent=2)
    print("  Contacts saved.")

def load_contacts():
    """Load contacts from JSON. Return empty dict if file missing."""
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
            print("  Contacts loaded.")
            return data
    except FileNotFoundError:
        return {}

def save_logs(action):
    """Append timestamped action to log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOGS, "a") as f:
        f.write(f"[{timestamp}] {action}\n")