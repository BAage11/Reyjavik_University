# Blaðsíða 162 - Code Listing 2.20

# while-else
# Simple guessing game: start with a random number and
# guess with hints until:
#   guess is correct
#   the guess is out of range indicating the user is quitting
# All non-typed variables are integers.

import random
# Get the random number module

number = random.randint(0,10)
# Get a random number between 0 and 10 inclusive

print("Hi-Lo Number Guessing Game: between 0 and 10 inclusive.")
print()

guess_str = input("Guess a number: ")
# Get an initial guess

guess = int(guess_str)
# convert string to number

# While guess is range, keep asking
while 0 <= guess <= 10:
  if guess > number:
    print("Guessed Too High.")
  elif guess < number:
    print("Guessed too Low.")
  else:                 # Correct guess, exit with break
    print("You guessed it. The number was:", number)
    break
  # Keep going, get the next guess
  guess_str = input("Guess a number: ")
  guess = int(guess_str)
else:
  print("You quit early, the number was:", number)
