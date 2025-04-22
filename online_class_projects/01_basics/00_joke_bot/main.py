PROMPT:str = "What do you want? "
JOKE:str = "I'm not lazy, I'm on energy-saving mode. 😎🔋"
SORRY:str = "Sorry, I only tell jokes"

def main():
    user_input = input(PROMPT).lower()
    user_input = user_input.strip()

    if "joke" in user_input:
        print(JOKE)
    else: 
        print(SORRY)

if __name__ == "__main__":
    main()           