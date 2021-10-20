import random
import time

# trial 5 questions to work out kinks in code:
quiz_answers = [
  {
    "question": {
      "swedish": "vecka (n)",
      "english": "week"
    },
    "answer": {
      "a": "valley",
      "b": "wiggle",
      "c": "week",
      "d": "travel",
      "correct": "c",
      "swedish": "vecka (n)"
    }
  },
  {
    "question": {
      "swedish": "år (n)",
      "english": "year"
    },
    "answer": {
      "a": "oar",
      "b": "ore",
      "c": "or",
      "d": "year",
      "correct": "d",
      "swedish": "år (n)"
    }
  },
  {
    "question": {
      "swedish": "idag (n)",
      "english": "today"
    },
    "answer": {
      "a": "dog",
      "b": "cod",
      "c": "today",
      "d": "day",
      "correct": "c",
      "swedish": "idag (n)"
    }
  },
  {
    "question": {
      "swedish": "imorgon (n)",
      "english": "tomorrow"
    },
    "answer": {
      "a": "air gun",
      "b": "organ",
      "c": "tomorrow",
      "d": "mirror",
      "correct": "c",
      "swedish": "imorgon (n)"
    }
  },
  {
    "question": {
      "swedish": "igår (n)",
      "english": "yesterday"
    },
    "answer": {
      "a": "eagle",
      "b": "yesterday",
      "c": "ogre",
      "d": "igloo",
      "correct": "b",
      "swedish": "igår (n)"
    }
  }
]

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
        card_sets.append(quiz_answers[random_number])
        i += 1


display_cards()

# quiz section:
print("QUIZ!")

questions = [card["question"] for card in card_sets]
answers = [card["answer"] for card in card_sets]

# prints out the question to the user:
for question in questions:
    print(f'Swedish word: {question["swedish"]}, English word: {question["english"]}')
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
score = 0
for answer in answers:
    print(f'What is the English word for: {answer["swedish"]}?')
    print('Enter a letter for the correct answer (a, b, c, or d).')
    print(f' Is it {answer["a"]}, {answer["b"]}, {answer["c"]}, or {answer["d"]}?')
    user_input = input().lower()
if user_input == answer["correct"]:
    print("That is correct!")
    score += 1
else:
    print("Sorry! Wrong answer.")
    score -= 1
    print("Your score: ")
    print(score)
