
import random  

def mad_libs():
    
    adjective = input("Enter an adjective: ")  
    noun = input("Enter a noun: ")  
    verb = input("Enter a verb: ")  
    place = input("Enter a place: ")  

    
    stories = [
        f"One day, a {adjective} {noun} decided to {verb} all the way to the {place}.",
        f"In a {adjective} village, there lived a {noun} who loved to {verb}.",
        f"The {adjective} {noun} was bored, so it decided to {verb} at the {place}.",
        f"A {adjective} {noun} once visited the {place} and started to {verb}."
    ]
    story = random.choice(stories)

    
    print("\nHere is your Mad Libs story:\n")
    print(story)


mad_libs()

