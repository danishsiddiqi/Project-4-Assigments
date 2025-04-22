import random


def guess_number():
    print("I am thinking of a number between 1 and 100.")
    guess_number = random.randint(1 , 100)

    guess = int(input("Enter your guess: "))

    while guess != guess_number:
        if guess < guess_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        guess = int(input("Enter your guess: "))

        print()
        guess = int(input("Enter a new guess: "))
    print("Congratulations! You guessed the number.")
if __name__ == "__main__":
    guess_number()    


  
