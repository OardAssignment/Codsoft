# class Contact:
#     def __init__(self, name, phone_number, email, address):
#         self.name = name
#         self.phone_number = phone_number
#         self.email = email
#         self.address = address

# class ContactManager:
#     def __init__(self):
#         self.contacts = []

#     def add_contact(self, name, phone_number, email, address):
#         contact = Contact(name, phone_number, email, address)
#         self.contacts.append(contact)

#     def view_contacts(self):
#         if len(self.contacts) == 0:
#             print("No contacts found.")
#         else:
#             for contact in self.contacts:
#                 print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")

#     def search_contacts(self, keyword):
#         found_contacts = []
#         for contact in self.contacts:
#             if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
#                 found_contacts.append(contact)
#         if len(found_contacts) == 0:
#             print("No contacts found.")
#         else:
#             for contact in found_contacts:
#                 print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")

#     def update_contact(self, name, phone_number, email, address):
#         for contact in self.contacts:
#             if contact.name == name:
#                 contact.phone_number = phone_number
#                 contact.email = email
#                 contact.address = address
#                 print("Contact updated successfully.")
#                 return
#         print("Contact not found.")

#     def delete_contact(self, name):
#         for contact in self.contacts:
#             if contact.name == name:
#                 self.contacts.remove(contact)
#                 print("Contact deleted successfully.")
#                 return
#         print("Contact not found.")


# contact_manager = ContactManager()


# contact_manager.add_contact("John Doe", "1234567890", "john@example.com", "123 Main St")
# contact_manager.add_contact("Jane Smith", "9876543210", "jane@example.com", "456 Elm St")


# contact_manager.view_contacts()


# contact_manager.search_contacts("John")


# contact_manager.update_contact("John Doe", "5555555555", "john.doe@example.com", "789 Oak St")

# # Delete contact
# contact_manager.delete_contact("Jane Smith")


class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contacts(self, keyword):
        results = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                results.append(contact)
        return results

    def update_contact(self, index, new_contact):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = new_contact
            print("Contact updated successfully.")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            deleted_contact = self.contacts.pop(index)
            print(f"Contact '{deleted_contact.name}' deleted successfully.")
        else:
            print("Invalid contact index.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_manager.add_contact(new_contact)

        elif choice == "2":
            contact_manager.view_contacts()

        elif choice == "3":
            keyword = input("Enter name or phone number to search: ")
            results = contact_manager.search_contacts(keyword)
            if not results:
                print("No matching contacts found.")
            else:
                print("Matching Contacts:")
                for i, contact in enumerate(results, start=1):
                    print(f"{i}. Name: {contact.name}, Phone: {contact.phone_number}")

        elif choice == "4":
            index = int(input("Enter the index of the contact to update: "))
            if 0 <= index < len(contact_manager.contacts):
                name = input("Enter new name: ")
                phone_number = input("Enter new phone number: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                new_contact = Contact(name, phone_number, email, address)
                contact_manager.update_contact(index, new_contact)
            else:
                print("Invalid contact index.")

        elif choice == "5":
            index = int(input("Enter the index of the contact to delete: "))
            contact_manager.delete_contact(index)

        elif choice == "6":
            print("Exiting the Contact Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
