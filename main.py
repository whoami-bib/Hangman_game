# This is a sample hangman game sample
import random

from stages import stages, logo
from word_list import word_list

print(logo)
no_of_life = 6

display = []
chosen_word = random.choice(word_list)
for i in range(len(chosen_word)):
    display.append("_")
print(display)
end_of_game = False

while not end_of_game:
    guess = input("enter a letter")
    if guess in display:
        print(f"you have already entered the letter {guess}")
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = guess
            print(display)
        if "_" not in display:
            end_of_game = True
            print("You have won")
            # print(display)
    if guess not in chosen_word:
        print(f"you have guessed {guess} which is not in the word.You lose a life")
        no_of_life -= 1
        if no_of_life == 0:
            end_of_game = True
            print("out of lives")
    print(stages[no_of_life])
