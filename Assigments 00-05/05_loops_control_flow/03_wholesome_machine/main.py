AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():
    print(f"Please type the following Affirmation: {AFFIRMATION}")
    while True:
        user_input = input("Type here: ")
        if user_input == AFFIRMATION:
            print("Correct!")
            break
        else:
            print("That was not the correct Affirmation.")


if __name__ == "__main__":
    main()