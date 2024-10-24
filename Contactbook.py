import re

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        if name in self.contacts:
            self.contacts[name] += ", " + phone
            print(f"Phone number '{phone}' added for contact '{name}' successfully.")
        else:
            self.contacts[name] = phone
            print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        if self.contacts:
            print("Contacts:")
            for name, phone in self.contacts.items():
                print(f"Name: {name}, Phone: {phone}")
        else:
            print("No contacts found.")

    def edit_contact(self, name, new_phone):
        if name in self.contacts:
            self.contacts[name] += ", " + new_phone
            print(f"Phone number '{new_phone}' added for contact '{name}' successfully.")
        else:
            print(f"Contact '{name}' not found.")
    
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

def validate_phone(phone):
    pattern = r'^\d{10}$'
    return bool(re.match(pattern, phone))

def main():
    contact_book = ContactBook()

    while True:
        print("\n===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number (10 digits): ")
            if validate_phone(phone):
                contact_book.add_contact(name, phone)
            else:
                print("Invalid phone number format. Please enter 10 digits.")
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            name = input("Enter name of contact to edit: ")
            if name in contact_book.contacts:
                new_phone = input("Enter new phone number (10 digits): ")
                if validate_phone(new_phone):
                    contact_book.edit_contact(name, new_phone)
                else:
                    print("Invalid phone number format. Please enter 10 digits.")
            else:
                print(f"Contact '{name}' not found.")
        elif choice == '4':
            name = input("Enter name of contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
