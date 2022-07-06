import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

display = []

for letter in chosen_word:
    display += "_"
print(display)

end_game = False

mistakes = 6

lives = 6

while not end_game:
    
    guess = input("guess your letter").lower()
    
    for position in range(len(chosen_word)):
        
        if guess == chosen_word[position]:
            display[position] = guess
            print(display)
            
    if guess not in chosen_word:
        mistakes -= 1
        lives -= 1
        print(stages[mistakes])
        print("lives left:", lives)
    
    if mistakes == 0:
        end_game = True
        print("you lost")
            
    if "_" not in display:
        end_game = True
        print("you won")