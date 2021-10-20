import random
import time

# Flashcard 100 Basic Swedish words
# flashcards = {"flash_0": {"vecka (n)": "week"},
#              "flash_1": {"år (n)": "year"},
#              "flash_2": {"idag (adv)": "today"},
#              "flash_3": {"imorgon (adv)": "tomorrow"},
#              "flash_4": {"igår (adv)": "yesterday"},
#              "flash_5": {"kalender (n)": "calendar"},
#              "flash_6": {"sekund (n)": "second"},
#              "flash_7": {"timme (n)": "hour"},
#              "flash_8": {"minut (n)": "minute"},
#              "flash_9": {"klockan... (n)": "o'clock"},
#              "flash_10": {"klocka (n)": "clock"},
#              "flash_11": {"en timme (n)": "one hour"},
#              "flash_12": {"kan (v)": "can"},
#              "flash_13": {"använda (v)": "use"},
#              "flash_14": {"göra (v)": "do"},
#              "flash_15": {"gå (v)": "go"},
#              "flash_16": {"komma (v)": "come"},
#              "flash_17": {"skratta (v)": "laugh"},
#              "flash_18": {"göra (v)": "make"},
#              "flash_19": {"se (v)": "see"},
#              "flash_20": {"långt (adj)": "far"},
#              "flash_21": {"liten (adj)": "small"},
#              "flash_22": {"bra (adj)": "good"},
#              "flash_23": {"vacker (adj)": "beautiful"},
#              "flash_24": {"ful (adj)": "ugly"},
#              "flash_25": {"svår (adj)": "difficult"},
#              "flash_26": {"lätt (adj)": "easy"},
#              "flash_27": {"bra (adj)": "good"},
#              "flash_28": {"dålig (adj)": "bad"},
#              "flash_29": {"nära (adj)": "near"},
#              "flash_30": {"Trevligt att träffas.": "Nice to meet you."},
#              "flash_31": {"Hej.": "Hi."},
#              "flash_32": {"God morgon!": "Good morning!"},
#              "flash_33": {"Goddag.": "Good afternoon."},
#              "flash_34": {"God kväll": "Good evening."},
#              "flash_35": {"Godnatt.": "Good night."},
#              "flash_36": {"Hur mår du?": "How are you?"},
#              "flash_37": {"Tack!": "Thank you!"},
#              "flash_38": {"Nej.": "No."},
#              "flash_39": {"Jag är...[name].": "I'm... [name]."},
#              "flash_40": {"Hej då.": "Goodbye."},
#              "flash_41": {"Ja. (interj)": "Yes."},
#              "flash_42": {"måndag (n)": "Monday"},
#              "flash_43": {"tisdag (n)": "Tuesday"},
#              "flash_44": {"onsdag (n)": "Wednesday"},
#              "flash_45": {"torsdag (n)": "Thursday"},
#              "flash_46": {"fredag (n)": "Friday"},
#              "flash_47": {"lördag (n)": "Saturday"},
#              "flash_48": {"söndag (n)": "Sunday"},
#              "flash_49": {"januari (n)": "January"},
#              "flash_50": {"februari (n)": "February"},
#              "flash_51": {"mars (n)": "March"},
#              "flash_52": {"april (n)": "April"},
#              "flash_53": {"maj (n)": "May"},
#              "flash_54": {"juni (n)": "June"},
#              "flash_55": {"juli (n)": "July"},
#              "flash_56": {"augusti (n)": "August"},
#              "flash_57": {"september (n)": "September"},
#              "flash_58": {"november (n)": "November"},
#              "flash_59": {"december (n)": "December"},
#              "flash_60": {"noll": "zero"},
#              "flash_61": {"ett": "one"},
#              "flash_62": {"två": "two"},
#              "flash_63": {"tre": "three"},
#              "flash_64": {"fyra": "four"},
#              "flash_65": {"fem": "five"},
#              "flash_66": {"sex": "six"},
#              "flash_67": {"sju": "seven"},
#             "flash_68": {"åtta": "eight"},
#              "flash_69": {"nio": "nine"},
#              "flash_70": {"tio": "ten"},
#              "flash_71": {"kaffe (n)": "Coffee"},
#              "flash_72": {"té (n)": "Tea"},
#              "flash_73": {"öl (n)": "Beer"},
#              "flash_74": {"vin (n)": "Wine"},
#              "flash_75": {"vatten (n)": "Water"},
#              "flash_76": {"biff (n)": "Beef"},
#              "flash_77": {"fläsk (n)": "Pork"},
#              "flash_78": {"kyckling (n)": "Chicken"},
#              "flash_79": {"lamm (n)": "Lamb"},
#              "flash_80": {"fisk (n)": "Fish"},
#              "flash_81": {"fot (n)": "Foot"},
#              "flash_82": {"ben (n)": "Leg"},
#              "flash_83": {"huvud (n)": "Head"},
#              "flash_84": {"arm (n)": "Arm"},
#              "flash_85": {"hand (n)": "Hand"},
#              "flash_86": {"finger (n)": "Finger"},
#              "flash_87": {"kropp (n)": "Body"},
#              "flash_89": {"mage (n)": "Stomach"},
#              "flash_90": {"rygg (n)": "Back"},
#              "flash_91": {"sjuksköterska (n)": "Nurse"},
#              "flash_92": {"läkare (n)": "Doctor"},
#              "flash_93": {"poliskonstapel (n)": "Police Officer"},
#              "flash_94": {"kock (n)": "A cook/chef"},
#              "flash_95": {"ingenjör (n)": "Engineer"},
#              "flash_96": {"lärare (n)": "Teacher"},
#              "flash_97": {"programmerare (n)": "Programmer"},
#              "flash_98": {"försäljare (n)": "Salesman"},
#              "flash_99": {"snickare (n)": "Carpenter"}}

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
        random_number = random.randint(0, len(quiz_answers))
        card_sets.append(quiz_answers[random_number])
        i += 1


display_cards()

# quiz section:
print("QUIZ!")
questions = [card["question"] for card in card_sets]
answers = [card["answer"] for card in card_sets]
# prints out the question to the user:
for question in questions:
    print(question["swedish"], question["english"])
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
for answer in answers:
    print(answer["swedish"])
    print(answer["a"], answer["b"], answer["c"], answer["d"])
    user_input = input().lower()
if user_input == answer["correct"]:
    print("That is correct!")
else:
    print("Sorry! Wrong answer.")
