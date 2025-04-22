import random

def guess_the_number():
      print("🎮 Welcome to 'Guess the Number' Game! 🎯")
      print("I have selected a number between 1 and 100. Can you guess it?")

      secrete_number = random.randint(1, 100)
      attempts = 0

      while True:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secrete_number:
                  print("Too low! Try again.")
            elif guess > secrete_number:
                  print("Too high! Try again.")
            else:
                  print(f"🎉 Congratulations! You have guessed the number in {attempts} attempts.")
                  break
            



guess_the_number()



