import random

# Step 1: Predefined word list
words = ["apple", "tiger", "chair", "robot", "plant"]

# Step 2: Choose random word
word = random.choice(words)

# Step 3: Initialize variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

# Step 4: Create display (hidden word)
display = ["_"] * len(word)

print("🎮 Welcome to Hangman!")
print("Guess the word!")

# Step 5: Game loop
while incorrect_guesses < max_attempts and "_" in display:
    print("\nWord:", " ".join(display))
    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("✅ Correct guess!")

        # Reveal letters
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        incorrect_guesses += 1
        print("❌ Wrong guess!")
        print("Attempts left:", max_attempts - incorrect_guesses)

# Step 6: Result
if "_" not in display:
    print("\n🎉 You won! The word was:", word)
else:
    print("\n💀 You lost! The word was:", word)