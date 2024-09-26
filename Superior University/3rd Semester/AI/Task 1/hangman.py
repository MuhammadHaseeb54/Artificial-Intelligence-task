# Question 01
# Dynamic Hangman game
import random
def make_guess(guess):
    global attempt, score, selected_word
    if guess.lower() in selected_word:
        for index, letter in enumerate(selected_word):
            if letter == guess.lower():
                blank_list[index] = letter
        score += 10
        return True
    else:
        print(f"There is no '{guess}' in the word")
        attempt += 1  # Increase attempts for a wrong guess
        score -= 2
        return False
def get_difficulty():
    while True:
        level = input("Choose difficulty level (easy, medium, hard): ").lower()
        if level == 'easy':
            return word_list[:3]  # Easier words
        elif level == 'medium':
            return word_list[3:6]  # Medium difficulty words
        elif level == 'hard':
            return word_list[6:]  # Harder words
        else:
            print("Invalid choice. Please select again.")
def play_round():
    global attempt, score, selected_word, blank_list
    selected_word = random.choice(chosen_words)
    blank_list = ["_" for _ in selected_word]
    attempt = 0
    score = 0

    print("\n<<<<<<<<< New Round! >>>>>>>>>>>")
    while attempt < 7 and "_" in blank_list:
        print(hangman_stages[attempt])
        print("Current word:", ' '.join(blank_list))
        print("Current score:", score)
        guess = input("Welcome to Hangman! Make a guess: ")

        if len(guess) == 1 and guess.isalpha():
            make_guess(guess)
        else:
            print("Please enter a valid single letter.")

    if "_" not in blank_list:
        print("You win! ==> The word was:", selected_word)
    else:
        print("Game over! ==> The word was:", selected_word)
    print("Your score for this round is:", score)
    return score
hangman_stages = [
        '''  
  +---+
  |   |
      |
      |
      |
      |
=========''',
        '''  
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
        '''  
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
        '''  
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
        '''  
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''',
        '''  
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''',
        '''  
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========='''
    ]

word_list = ["programming", "coding", "computing", "python", "deepcode", "cloud", "datastructure", "modelreflexagent"]
chosen_words = get_difficulty()

total_score = 0
play_again = 'y'
print("\n------------------ Welcome to the Hangman ---------------------\n")
while play_again.lower() == 'y':
    total_score += play_round()
    play_again = input("Do you want to play another round? (y/n): ")

print("Thanks for playing! Your total score is:", total_score)

