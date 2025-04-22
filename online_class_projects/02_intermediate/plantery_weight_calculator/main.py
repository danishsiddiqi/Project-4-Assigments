def main ():
    earth_weight = float(input("Enter your weight on Earth (in kg): "))

    gravity_ratios = {
        "Mercury": 0.378,
        "Venus": 0.907,
        "Mars": 0.377,
        "Jupiter": 2.364,
        "Saturn": 0.916,
        "Uranus": 0.889,
        "Neptune": 1.125
    }

    print("\nSelect a planet to calculate your weight:\n")

    for planet in gravity_ratios:
        print(f"- {planet}")

    selected_planet = input("\nEnter the name of the planet: ").title()  

    if selected_planet in gravity_ratios:
        new_weight = earth_weight * gravity_ratios[selected_planet]  
        print(f"Your weight on {selected_planet} is {new_weight:.2f}kg")

    else:
        print("Invalid planet")

if __name__ == "__main__":
         main()       