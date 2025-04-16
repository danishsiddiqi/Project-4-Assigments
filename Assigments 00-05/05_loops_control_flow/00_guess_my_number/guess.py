import random

def guess_number():
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)

    guess = int(input("Enter a guess: "))

    while guess != number_to_guess:
        if guess < number_to_guess:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
            guess = int(input("Enter your guess: "))

        print()
        guess = int(input("Enter a new guess: ")) 

    print(f"Congratulations! You've guessed the number {number_to_guess}.")

if __name__ == "__main__":
    guess_number()

        
            