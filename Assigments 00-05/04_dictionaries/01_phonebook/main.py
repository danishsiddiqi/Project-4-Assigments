

phonebook = {}

def add_contact():
    while True:
        name = input("Enter contact name: ")
        if name == "":
            break
        number = input("Enter contact number: ")
        phonebook[name] = number
    print("\nContacts saved successfully!\n")

def display_phonebook():
    if not phonebook:
        print("Phonebook is empty.\n")
    else:
        print("\nSaved Contacts:")
        for name, number in phonebook.items():
            print(f"{name} -> {number}")
        print()

def lookup_contact():
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name in phonebook:
            print(phonebook[name])
        else:
            print(f"{name} is not in the phonebook")

print("=== Simple Phonebook Application ===\n")
add_contact()
display_phonebook()
lookup_contact()

print("\nThank you for using the phonebook!")
