#Step 1 
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

win = False

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
random_word = random.choice(word_list)

lives = len(stages) - 1

# print(random_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

n = len(random_word)

spaces = []

for i in range(0, n):
	spaces.append("_")

print(spaces)
print(f"Hint: {random_word}")

print(f"len of stages {len(stages)}")

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

def checkWin():
	for x in spaces:
		if x == "_":
			return False

	return True


while True:

	guess = input("Guess a letter: ").lower() 

	if (guess not in random_word):
		lives -= 1
		print("Sorry, wrong guess!")
		print(lives)
	else:
		print("You guessed it!")	

	for i in range(n):
		if (guess == random_word[i]):
			spaces[i] = guess

	print(spaces)	

	print(stages[lives])

	if "_" not in spaces:
		win = True	
		break;

	if (lives < 1):
		break;

if (win):
	print("You win!!")
else: 
	print("Sorry, You lose!")

print(random_word)
