def fruit_shop_calculator():
    # Fruit price list (fruit: price per piece)
    fruits = {
        "apple": 10.5,
        "orange": 10.0,
        "pomegranate": 25.0,
        "kiwi": 12.5,
        "banana": 2.0,
        "mango": 6.5
    }

    total_cost = 0.0

    print("Welcome to the fruit shop!")
    for fruit, price in fruits.items():
        quantity = int(input(f"How many ({fruit}) do you want?: "))
        cost = price * quantity
        total_cost += cost

    
    print(f"\nYour total is ${total_cost}")

fruit_shop_calculator()
