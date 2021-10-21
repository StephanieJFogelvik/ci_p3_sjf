import random
import time
from flashcards import quiz_answers


# ASCII Art by Max Strandberg - Swedisg flag:
def flag():
    print(" .^.")
    print("(( ))")
    print(" |#|_______________________________")
    print(" |#||########$$$###################|")
    print(" |#||########$$$###################|")
    print(" |#||########$$$###################|")
    print(" |#||########$$$###################|")
    print(" |#||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|")
    print(" |#||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|")
    print(" |#||########$$$###################|")
    print(" |#||########$$$###################|")
    print(" |#||########$$$###################|")
    print(" |#||########$$$###################|")
    print(' |#|'""""""""""""""""""""""""""""""'')
    print(" |#|")
    print(" |#|")
    print(" |#|")
    print(" |#|")
    print(" |#|")
    print(" |#|")
    print(" |#|")
    print(" |#|")
    print(" |#|")
    print(" |#|")
    print(" |#|")
    print(" |#|")
    print(" |#|")
    print(" |#|")
    print("//|\\")
    print('""""""""""""""""""""""""""""""""""""""')
    print(5 * "\n")


print("Flashcard Game for 100 Basic Swedish Words!")
print("")
print("")

# displays random flashcards for 3 seconds:
card_sets = []
print("READY?")


def display_cards():
    i = 1
    while i < 6:
        random_number = random.randint(0, len(quiz_answers)-1)
        if quiz_answers[random_number] not in card_sets:
            card_sets.append(quiz_answers[random_number])
            i += 1


display_cards()

# quiz section:
print("QUIZ!")

questions = [card["question"] for card in card_sets]
answers = [card["answer"] for card in card_sets]

# prints out the question to the user:
for question in questions:
    print(f'Swedish word: {question["swedish"]}, \
        English word: {question["english"]}')
    print("")
# puts a 3 sec pause between questions:
    time.sleep(3)
# input from the user to trigger multiple choice based on the quiz above:
print("Press Enter")
input()

print("Press Enter")
input()

# Enter Swe-flag image here (to push the flashcards out of view)

# Multiple choice questions:
SCORE = 0
for answer in answers:
    print(f'What is the English word for: {answer["swedish"]}?')
    print('Enter a letter for the correct answer (a, b, c, or d).')
    print(f' Is it {answer["a"]}, {answer["b"]}, {answer["c"]},\
         or {answer["d"]}?')
    user_input = input().lower()
if user_input == answer["correct"]:
    print("That is correct!")
    SCORE += 1
else:
    print("Sorry! Wrong answer.")
    SCORE -= 1
    print("Your score: ")
    print(SCORE)
