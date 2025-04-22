import random  


word_list = ["python", "hangman", "developer", "computer", "keyboard", "programming"]
word = random.choice(word_list)  
guessed_letters = []  
attempts = 6  


def display_word():
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

print("🎮 Welcome to Hangman! 🏆")
print(f"🔡 Your word: {display_word()}")

while attempts > 0:
    guess = input("🔠 Guess a letter: ").strip().lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Invalid input! Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
    else:
        print("❌ Wrong guess!")
        attempts -= 1

    print(f"📜 Word: {display_word()}")
    print(f"❤️ Attempts left: {attempts}")

    if "_" not in display_word():
        print("🎉 Congratulations! You guessed the word correctly! 🎯")
        break
else:
    print(f"😢 Game Over! The word was: {word}")
