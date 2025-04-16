def count_number():
    numbers = []        
    number_counts = {}    

    while True:
        user_input = input("Enter a number (or press Enter to finish): ")
        if user_input == "":
            break

        number = int(user_input)
        numbers.append(number)

    
        print("Numbers so far:", '{' + ', '.join(map(str, numbers)) + '}')

    
    for number in set(numbers): 
        number_counts[number] = numbers.count(number)


    print("\nFinal Count:")
    for number, count in number_counts.items():
        if count == 1:
            print(f"{number} appears {count} time.")
        else:
            print(f"{number} appears {count} times.")


count_number()
