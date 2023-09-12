import os
filename = "contacts.txt"
contacts = {}

while True:
    print("\nChoose an action:")
    print("1 - Add contact")
    print("2 - View contacts")
    print("3 - Search contacts")
    print("4 - Save contacts")
    print("5 - Load contacts")
    print("6 - Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter a name: ")
        phone = input("Enter a phone number: ")
        contacts[name] = phone
        print(f"Contact '{name}' added.")
    elif choice == '2':
        if not contacts:
            print("No contacts found.")
        else:
            for name, phone in contacts.items():
                print(f"Name: {name}, Phone: {phone}")
    elif choice == '3':
        search_name = input("Enter a name to search: ")
        if search_name in contacts:
            print(f"Name: {search_name}, Phone: {contacts[search_name]}")
        else:
            print(f"Contact '{search_name}' not found.")
    elif choice == '4':
        with open(filename, 'w') as file:
            for name, phone in contacts.items():
                file.write(f"{name},{phone}\n")
        print("Contacts saved.")
    elif choice == '5':
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                contacts.clear()
                for line in file:
                    name, phone = line.strip().split(',')
                    contacts[name] = phone
            print("Contacts loaded.")
        else:
            print("No saved contacts found.")
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please select a valid option.")
