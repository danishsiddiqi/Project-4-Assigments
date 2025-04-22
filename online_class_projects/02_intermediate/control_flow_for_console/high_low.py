import random

rounds = 5


def main():
    print("Welcome to the High Low game!")

    your_score = 0

    for i in range(your_score):
        print("Round" , i + 1)


    computer_number: int = random.randint(1,100) 
    your_number: int = random.randint(1,100) 
    print("your number is" , your_number)

    choice:str = input("Do you think that your nummber is higher or lower than computer number? ")

    higher_and_correct:bool = choice == "higher" and your_number > computer_number
    lower_and_correct:bool = choice == "lower" and your_number < computer_number

    if higher_and_correct and lower_and_correct:
        print("YOu are right, The Computer number was" , computer_number)

    else:
        print("That's Incorrect, the computer number was", computer_number)

    print("Your score is now", your_score)
    print()

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
   
            

       
       


 
