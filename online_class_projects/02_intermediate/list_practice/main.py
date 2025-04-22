my_list = ["red", "blue", "green", "yellow"]

def access_element(my_list, index):
    if 0 <= index < len(my_list):
        return f"Element at index {index}: {my_list[index]}"
    else:
        print("Index out of range")

def modify_element(my_list, index, new_value):
    if 0 <= index < len(my_list):
        old_value = my_list[index]
        my_list[index] = new_value
        return f"Element at index {index}: modified from {old_value} to {new_value}"
    else:
        print("Index out of range")

def slice_list(my_list, start_index, end_index):
    if 0 <= start_index < len(my_list) and 0 <= end_index <= len(my_list):
        return f"Sliced list: {my_list[start_index:end_index]}"
    else:
        print("Index out of range")

def list_game():
    print("🎮 Welcome to the List Game! 🎮")
    while True:
        print("\nCurrent list:", my_list)
        print("Choose an option:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            index = int(input("Enter the index of the element you want to access: "))
            result = access_element(my_list, index)
            if result: print(result)

        elif choice == "2":
            index = int(input("Enter the index of the element you want to modify: "))
            new_value = input("Enter the new value: ")
            result = modify_element(my_list, index, new_value)
            if result: print(result)

        elif choice == "3":
            start = int(input("Enter the start index for slice: "))
            end = int(input("Enter the end index for slice: "))
            result = slice_list(my_list, start, end)
            if result: print(result)

        elif choice == "4":
            print("🚪 Exiting the game. Thanks for playing!")
            break

        else:
            print("❌ Invalid choice. Please select a number between 1 to 4.")

# Only runs if this file is the main program
if __name__ == "__main__":
    list_game()
