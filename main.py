from list import word_list # Imports a word list from https://github.com/Xethron/Hangman/blob/master/words.txt
import random
import time


final_word = word_list[random.randint(0, 850)]
final_word_array = [] # Initialising string as a list
for i in final_word:
  final_word_array.append(i)
# A placeholder word for user to see how long word is
placeholder =  ""
guessed_word = []
for letter in range(len(final_word)):
  placeholder += "_ " # What the user sees
  guessed_word.append("_")

# Introduction
print("Welcome to Bens Brain Game! This is a hangman game where you have to guess the word. But be careful, if you get 5 letters wrong... YOU ARE OUT !!!")
time.sleep(1)
print("Okay now lets start to play the game!")
time.sleep(1)
# Main algorithm for game
error_count = 0 # Initialises error count
# Initialises dummy variable x
# x value goes through array to check if letter is in the word
x=0
correct_count = 0
guessed_letters = []
print(placeholder) # Shows user how long word is
while guessed_word != final_word:
  a = False # Initialises boolean value to dummy variable a
  letter = input("Guess one letter of the word ")
  # Checks if you guess 1 letter
  if letter in guessed_letters:
    print("You have already guessed that silly! Try again")
    time.sleep(1)
    continue
  if len(letter) > 1:
    print("Guess only one letter silly!")
    time.sleep(1)
    continue
  if letter.isalpha() == False:
    print("Guess a letter silly!")
    time.sleep(1)
    continue
  guessed_letters.append(letter)
  
  if x > len(final_word_array)-1:
      x=0

  letter_check = False
  for i in final_word_array: # Goes through word to see if letter is in word
    if letter == i:
      a = True
      if letter_check == False:
        print("Wow you got it right!")
        letter_check = True
      guessed_word[x] = letter # Replaces the letter in the position of the word
      correct_count += 1
    x += 1
  
  # Win condition
  if correct_count == len(final_word_array):
    print("Wow you are really good at this game!")
    time.sleep(1)
    retry_question = input("Would you like to play again? ")
    # Retry 'mechanic'
    if retry_question.lower() == 'yes':
      print("Alright get ready for another round!")
      time.sleep(1)
      print("Press the run button to play again silly!")
      time.sleep(1)
      quit()
    elif retry_question.lower() == 'no':
      print("Oh shucks! Thats such a shame. Have a great day!")
      time.sleep(1)
      quit()
    else:
      print("I am guessing thats a no. If you really want to play again run main.py again :) " )
      quit()

  # Lose condition
  if a == False:
    error_count += 1
    print(f'Wow you have gotten {error_count} wrong!')    
  if error_count == 7:
    print("Oh no it looks like you lost!")
    time.sleep(1)
    print(f"The word was '{final_word}'!")
    quit()
  
  display_word = ''
  for i in guessed_word:
    display_word += f'{i} '
  print(display_word)