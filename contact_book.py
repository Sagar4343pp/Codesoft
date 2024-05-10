class Contact:
    def add_details(self, name, phone):
        self.name = name
        self.phone = phone
    
def add_contact(contacts, name, phone):
    contact = Contact()
    contact.add_details(name, phone)
    contacts.append(contact)

def view_contacts(contacts):
    print("Contact List:")
    if not contacts:
        print("No contacts to display.")
    else:
        for contact in contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")
        
def search_contact(contacts, query):
    for contact in contacts:
        if query.lower() in contact.name.lower() or query in contact.phone:
            print(f"Name: {contact.name}, Phone: {contact.phone}")

def update_contact(contacts, name, new_phone):
    for contact in contacts:
        if contact.name.lower() == name.lower():
            contact.phone = new_phone
            print("Contact updated successfully.......")
            return
    print("Contact not found...........")

def delete_contact(contacts, name):
    for contact in contacts:
        if contact.name.lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully.........")
            return
    print("Contact not found.")

contacts = []
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    

    choice = input('Enter Your Choice:  ')

    if choice == '1':
        name = input('Enter Name:   ')
        phone = input('Enter Mobile Number: ')
        add_contact(contacts, name, phone)
    elif choice == '2':
        view_contacts(contacts)
    elif choice == '3':
        query = input("Enter name or phone number to search: ")
        search_contact(contacts, query)
    elif choice == "4":
        name = input("Enter name of contact to update: ")
        new_phone = input("Enter new phone number: ")
        update_contact(contacts, name, new_phone)
    elif choice == "5":
        name = input("Enter name of contact to delete: ")
        delete_contact(contacts, name)

    elif choice == "6":
        break