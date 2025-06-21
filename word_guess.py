import random
def get_random_word():
    words = ["python", "java", "kotlin", "javascript","HTML", "CSS", "ruby", "swift", "typescript", "go"]
    return random.choice(words)
def word_status(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display
def play_game():
    word = get_random_word()
    guessed_letters = []
    attempts = 10

    print("Welcome to the Word Guessing Game!")
    print("Try to guess the word. You have 6 attempts.")
    print("Secret word :",word_status(word, guessed_letters))

    while attempts > 0:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        current_status = word_status(word, guessed_letters)
        print("Current word status:", current_status)

        if "_" not in current_status:
            print("Congratulations! You've guessed the word:", word)
            return
if __name__ == "__main__":
         play_game()        
    