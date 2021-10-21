import random
import time


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


# 100 basic Swedish words and phrases, with possible answers:
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
    },
    {
        "question": {
            "swedish": "kalender",
            "english": "calendar"
        },
        "answer": {
            "a": "cylinder",
            "b": "calendar",
            "c": "commander",
            "d": "colander",
            "correct": "b",
            "swedish": "kalender"
        }
    },
    {
        "question": {
            "swedish": "sekund",
            "english": "second"
        },
        "answer": {
            "a": "second",
            "b": "succumbed",
            "c": "typhoon",
            "d": "sickened",
            "correct": "a",
            "swedish": "sekund"
        }
    },
    {
        "question": {
            "swedish": "timme",
            "english": "hour"
        },
        "answer": {
            "a": "tonne",
            "b": "hour",
            "c": "thimble",
            "d": "teeming",
            "correct": "b",
            "swedish": "hour"
        }
    },
    {
        "question": {
            "swedish": "minut",
            "english": "Minute"
        },
        "answer": {
            "a": "small",
            "b": "well",
            "c": "minute",
            "d": "magnet",
            "correct": "c",
            "swedish": "minut"
        }
    },
    {
        "question": {
            "swedish": "klockan...",
            "english": "...o'clock"
        },
        "answer": {
            "a": "knocking",
            "b": "clock in",
            "c": "cooking",
            "d": "...o'clock",
            "correct": "d",
            "swedish": "klockan..."
        }
    },
    {
        "question": {
            "swedish": "klocka",
            "english": "Clock"
        },
        "answer": {
            "a": "cloak",
            "b": "click",
            "c": "clock",
            "d": "clog",
            "correct": "c",
            "swedish": "klocka"
        }
    },
    {
        "question": {
            "swedish": "en timme",
            "english": "one hour"
        },
        "answer": {
            "a": "in time",
            "b": "ending",
            "c": "on time",
            "d": "one hour",
            "correct": "d",
            "swedish": "en timme"
        }
    },
    {
        "question": {
            "swedish": "kan",
            "english": "can"
        },
        "answer": {
            "a": "kin",
            "b": "con",
            "c": "can",
            "d": "ban",
            "correct": "c",
            "swedish": "kan"
        }
    },
    {
        "question": {
            "swedish": "använda",
            "english": "use"
        },
        "answer": {
            "a": "invade",
            "b": "use",
            "c": "antenna",
            "d": "envied",
            "correct": "b",
            "swedish": "använda"
        }
    },
    {
        "question": {
            "swedish": "göra",
            "english": "do"
        },
        "answer": {
            "a": "grow",
            "b": "do",
            "c": "grey",
            "d": "sew",
            "correct": "b",
            "swedish": "göra"
        }
    },
    {
        "question": {
            "swedish": "gå",
            "english": "go"
        },
        "answer": {
            "a": "go",
            "b": "so",
            "c": "do",
            "d": "eye",
            "correct": "a",
            "swedish": "gå"
        }
    },
    {
        "question": {
            "swedish": "komma",
            "english": "come"
        },
        "answer": {
            "a": "comma",
            "b": "common",
            "c": "calmly",
            "d": "come",
            "correct": "d",
            "swedish": "komma"
        }
    },
    {
        "question": {
            "swedish": "skratta",
            "english": "laugh"
        },
        "answer": {
            "a": "skirt",
            "b": "squat",
            "c": "laugh",
            "d": "rake",
            "correct": "c",
            "swedish": "skratta"
        }
    },
    {
        "question": {
            "swedish": "säga",
            "english": "say"
        },
        "answer": {
            "a": "thing",
            "b": "roof",
            "c": "say",
            "d": "write",
            "correct": "c",
            "swedish": "säga"
        }
    },
    {
        "question": {
            "swedish": "se",
            "english": "see"
        },
        "answer": {
            "a": "soothe",
            "b": "sea",
            "c": "see",
            "d": "fee",
            "correct": "c",
            "swedish": "se"
        }
    },
    {
        "question": {
            "swedish": "långt",
            "english": "far"
        },
        "answer": {
            "a": "light",
            "b": "far",
            "c": "lead",
            "d": "narrow",
            "correct": "b",
            "swedish": "långt"
        }
    },
    {
        "question": {
            "swedish": "liten",
            "english": "small"
        },
        "answer": {
            "a": "lightweight",
            "b": "bottle",
            "c": "dog",
            "d": "small",
            "correct": "d",
            "swedish": "liten"
        }
    },
    {
        "question": {
            "swedish": "stor",
            "english": "big"
        },
        "answer": {
            "a": "steer",
            "b": "big",
            "c": "house",
            "d": "horse",
            "correct": "b",
            "swedish": "stor"
        }
    },
    {
        "question": {
            "swedish": "vacker",
            "english": "beautiful"
        },
        "answer": {
            "a": "mirror",
            "b": "beautiful",
            "c": "stairwell",
            "d": "ceiling",
            "correct": "b",
            "swedish": "vacker"
        }
    },
    {
        "question": {
            "swedish": "ful",
            "english": "ugly"
        },
        "answer": {
            "a": "full",
            "b": "pretty",
            "c": "bottle",
            "d": "ugly",
            "correct": "d",
            "swedish": "ful"
        }
    },
    {
        "question": {
            "swedish": "svår",
            "english": "difficult"
        },
        "answer": {
            "a": "heavy",
            "b": "difficult",
            "c": "sore",
            "d": "sad",
            "correct": "b",
            "swedish": "svår"
        }
    },
    {
        "question": {
            "swedish": "lätt",
            "english": "easy"
        },
        "answer": {
            "a": "butter",
            "b": "easy",
            "c": "ticket",
            "d": "cloud",
            "correct": "b",
            "swedish": "lätt"
        }
    },
    {
        "question": {
            "swedish": "bra",
            "english": "good"
        },
        "answer": {
            "a": "good",
            "b": "brother",
            "c": "brew",
            "d": "borough",
            "correct": "a",
            "swedish": "bra"
        }
    },
    {
        "question": {
            "swedish": "dålig",
            "english": "bad"
        },
        "answer": {
            "a": "good",
            "b": "radio",
            "c": "expensive",
            "d": "bad",
            "correct": "d",
            "swedish": "dålig"
        }
    },
    {
        "question": {
            "swedish": "nära",
            "english": "near"
        },
        "answer": {
            "a": "near",
            "b": "far",
            "c": "nerve",
            "d": "know",
            "correct": "a",
            "swedish": "nära"
        }
    },
    {
        "question": {
            "swedish": "Trevligt att träffas.",
            "english": "Nice to meet you."
        },
        "answer": {
            "a": "Please excuse me.",
            "b": "Nice to meet you.",
            "c": "This is my stop.",
            "d": "Nice weather today.",
            "correct": "b",
            "swedish": "Trevligt att träffas"
        }
    },
    {
        "question": {
            "swedish": "Hej",
            "english": "Hi"
        },
        "answer": {
            "a": "Soup",
            "b": "hedge",
            "c": "Wall",
            "d": "Hi",
            "correct": "d",
            "swedish": "Hej"
        }
    },
    {
        "question": {
            "swedish": "God morgon!",
            "english": "Good morning!"
        },
        "answer": {
            "a": "Good afternoon!",
            "b": "Good day!",
            "c": "Good moron!",
            "d": "Good morning!",
            "correct": "d",
            "swedish": "God morgon!"
        }
    },
    {
        "question": {
            "swedish": "Goddag.",
            "english": "Good afternoon."
        },
        "answer": {
            "a": "Good dog.",
            "b": "How gaudy.",
            "c": "Good afternoon.",
            "d": "Good night.",
            "correct": "c",
            "swedish": "Goddag."
        }
    },
    {
        "question": {
            "swedish": "God kväll.",
            "english": "Good evening."
        },
        "answer": {
            "a": "Good morning.",
            "b": "Good job.",
            "c": "Good day.",
            "d": "Good evening.",
            "correct": "d",
            "swedish": "God kväll."
        }
    },
    {
        "question": {
            "swedish": "Godnatt.",
            "english": "Good night."
        },
        "answer": {
            "a": "Hello.",
            "b": "Good day.",
            "c": "Bye.",
            "d": "Good night.",
            "correct": "d",
            "swedish": "Godnatt"
        }
    },
    {
        "question": {
            "swedish": "Hur mår du?",
            "english": "How are you?"
        },
        "answer": {
            "a": "How many do you want [to buy]?",
            "b": "What is that?",
            "c": "Where are we?",
            "d": "How are you?",
            "correct": "d",
            "swedish": "Hur mår du?"
        }
    },
    {
        "question": {
            "swedish": "tack",
            "english": "thanks"
        },
        "answer": {
            "a": "take",
            "b": "talk",
            "c": "stack",
            "d": "thanks",
            "correct": "d",
            "swedish": "tack"
        }
    },
    {
        "question": {
            "swedish": "nej",
            "english": "no"
        },
        "answer": {
            "a": "yes",
            "b": "neigh",
            "c": "sorry",
            "d": "no",
            "correct": "d",
            "swedish": "nej"
        }
    },
    {
        "question": {
            "swedish": "Jag är...[__]",
            "english": "I am...[name]"
        },
        "answer": {
            "a": "I am...[__]",
            "b": "I want...[__]",
            "c": "I went to...[__]",
            "d": "I saw...[__]",
            "correct": "a",
            "swedish": "Jag är...[__]"
        }
    },
    {
        "question": {
            "swedish": "Hej då",
            "english": "Goodbye"
        },
        "answer": {
            "a": "Hello",
            "b": "Goodbye",
            "c": "Tallyho",
            "d": "Cheers",
            "correct": "b",
            "swedish": "Hej då"
        }
    },
    {
        "question": {
            "swedish": "ja",
            "english": "yes"
        },
        "answer": {
            "a": "yes",
            "b": "maybe",
            "c": "elk",
            "d": "roar",
            "correct": "a",
            "swedish": "ja"
        }
    },
    {
        "question": {
            "swedish": "måndag",
            "english": "monday"
        },
        "answer": {
            "a": "Mad dog",
            "b": "Monday",
            "c": "Mattock",
            "d": "May Day",
            "correct": "b",
            "swedish": "måndag"
        }
    },
    {
        "question": {
            "swedish": "tisdag",
            "english": "tuesday"
        },
        "answer": {
            "a": "today",
            "b": "teddy",
            "c": "tuesday",
            "d": "toothy",
            "correct": "c",
            "swedish": "tisdag"
        }
    },
    {
        "question": {
            "swedish": "onsdag",
            "english": "wednesday"
        },
        "answer": {
            "a": "twenty",
            "b": "wander",
            "c": "wheezy",
            "d": "wednesday",
            "correct": "d",
            "swedish": "onsdag"
        }
    },
    {
        "question": {
            "swedish": "torsdag",
            "english": "thursday"
        },
        "answer": {
            "a": "thursday",
            "b": "third day",
            "c": "thready",
            "d": "thorough",
            "correct": "a",
            "swedish": "torsdag"
        }
    },
    {
        "question": {
            "swedish": "fredag",
            "english": "friday"
        },
        "answer": {
            "a": "flighty",
            "b": "friday",
            "c": "friary",
            "d": "fried food",
            "correct": "b",
            "swedish": "fredag"
        }
    },
    {
        "question": {
            "swedish": "lördag",
            "english": "saturday"
        },
        "answer": {
            "a": "lower deck",
            "b": "arctic",
            "c": "lördag",
            "d": "burdock",
            "correct": "c",
            "swedish": "lördag"
        }
    },
    {
        "question": {
            "swedish": "söndag",
            "english": "sunday"
        },
        "answer": {
            "a": "sundog",
            "b": "snake",
            "c": "sandbag",
            "d": "sunday",
            "correct": "d",
            "swedish": "söndag"
        }
    },
    {
        "question": {
            "swedish": "januari",
            "english": "January"
        },
        "answer": {
            "a": "January",
            "b": "Janissary",
            "c": "Annuary",
            "d": "Yearbook",
            "correct": "a",
            "swedish": "januari"
        }
    },
    {
        "question": {
            "swedish": "februari",
            "english": "February"
        },
        "answer": {
            "a": "Fibulare",
            "b": "February",
            "c": "Fever",
            "d": "Fibbing",
            "correct": "b",
            "swedish": "februari"
        }
    },
    {
        "question": {
            "swedish": "mars",
            "english": "March"
        },
        "answer": {
            "a": "Mare",
            "b": "Morse",
            "c": "March",
            "d": "War",
            "correct": "c",
            "swedish": "mars"
        }
    },
    {
        "question": {
            "swedish": "april",
            "english": "April"
        },
        "answer": {
            "a": "Apron",
            "b": "Opal",
            "c": "Apple",
            "d": "April",
            "correct": "d",
            "swedish": "april"
        }
    },
    {
        "question": {
            "swedish": "maj",
            "english": "May"
        },
        "answer": {
            "a": "May",
            "b": "Match",
            "c": "Merge",
            "d": "Nudge",
            "correct": "a",
            "swedish": "maj"
        }
    },
    {
        "question": {
            "swedish": "juni",
            "english": "June"
        },
        "answer": {
            "a": "Uni",
            "b": "June",
            "c": "Goon",
            "d": "Join me",
            "correct": "b",
            "swedish": "juni"
        }
    },
    {
        "question": {
            "swedish": "juli",
            "english": "July"
        },
        "answer": {
            "a": "Pretty",
            "b": "Genie",
            "c": "July",
            "d": "a small fishing vessel",
            "correct": "c",
            "swedish": "juli"
        }
    },
    {
        "question": {
            "swedish": "september",
            "english": "September"
        },
        "answer": {
            "a": "Septum",
            "b": "Timber",
            "c": "Foul-tempered",
            "d": "September",
            "correct": "d",
            "swedish": "september"
        }
    },
    {
        "question": {
            "swedish": "november",
            "english": "November"
        },
        "answer": {
            "a": "November",
            "b": "Novelty",
            "c": "Notorious",
            "d": "Nevermore",
            "correct": "a",
            "swedish": "november"
        }
    },
    {
        "question": {
            "swedish": "december",
            "english": "December"
        },
        "answer": {
            "a": "Cucumber",
            "b": "December",
            "c": "Dissemble",
            "d": "Dishonour",
            "correct": "b",
            "swedish": "december"
        }
    },
    {
        "question": {
            "swedish": "noll",
            "english": "zero"
        },
        "answer": {
            "a": "knoll",
            "b": "Nile",
            "c": "zero",
            "d": "kneel",
            "correct": "c",
            "swedish": "noll"
        }
    },
    {
        "question": {
            "swedish": "ett",
            "english": "one"
        },
        "answer": {
            "a": "it",
            "b": "out",
            "c": "when",
            "d": "one",
            "correct": "d",
            "swedish": "ett"
        }
    },
    {
        "question": {
            "swedish": "två",
            "english": "two"
        },
        "answer": {
            "a": "two",
            "b": "tea",
            "c": "tee",
            "d": "tow",
            "correct": "a",
            "swedish": "två"
        }
    },
    {
        "question": {
            "swedish": "tre",
            "english": "three"
        },
        "answer": {
            "a": "tray",
            "b": "three",
            "c": "true",
            "d": "tree",
            "correct": "b",
            "swedish": "three"
        }
    },
    {
        "question": {
            "swedish": "fyra",
            "english": "four"
        },
        "answer": {
            "a": "fiery",
            "b": "ferry",
            "c": "four",
            "d": "free",
            "correct": "c",
            "swedish": "fyra"
        }
    },
    {
        "question": {
            "swedish": "fem",
            "english": "five"
        },
        "answer": {
            "a": "femme",
            "b": "foam",
            "c": "fawn",
            "d": "five",
            "correct": "d",
            "swedish": "fem"
        }
    },
    {
        "question": {
            "swedish": "sex",
            "english": "six"
        },
        "answer": {
            "a": "six",
            "b": "socks",
            "c": "sax",
            "d": "sects",
            "correct": "a",
            "swedish": "sex"
        }
    },
    {
        "question": {
            "swedish": "sju",
            "english": "seven"
        },
        "answer": {
            "a": "sigh",
            "b": "seven",
            "c": "flu",
            "d": "sew",
            "correct": "b",
            "swedish": "sju"
        }
    },
    {
        "question": {
            "swedish": "åtta",
            "english": "eight"
        },
        "answer": {
            "a": "two",
            "b": "understand",
            "c": "eight",
            "d": "tie",
            "correct": "c",
            "swedish": "åtta"
        }
    },
    {
        "question": {
            "swedish": "nio",
            "english": "nine"
        },
        "answer": {
            "a": "neo",
            "b": "happy",
            "c": "meow",
            "d": "nine",
            "correct": "d",
            "swedish": "nio"
        }
    },
    {
        "question": {
            "swedish": "tio",
            "english": "ten"
        },
        "answer": {
            "a": "ten",
            "b": "tie",
            "c": "tile",
            "d": "thaw",
            "correct": "a",
            "swedish": "tio"
        }
    },
    {
        "question": {
            "swedish": "kaffe",
            "english": "coffee"
        },
        "answer": {
            "a": "coughing",
            "b": "coffee",
            "c": "calf",
            "d": "goof",
            "correct": "b",
            "swedish": "kaffe"
        }
    },
    {
        "question": {
            "swedish": "té",
            "english": "tea"
        },
        "answer": {
            "a": "thee",
            "b": "to",
            "c": "tea",
            "d": "he",
            "correct": "c",
            "swedish": "tea"
        }
    },
    {
        "question": {
            "swedish": "öl",
            "english": "beer"
        },
        "answer": {
            "a": "wool",
            "b": "ill",
            "c": "öwl",
            "d": "beer",
            "correct": "d",
            "swedish": "öl"
        }
    },
    {
        "question": {
            "swedish": "vin",
            "english": "wine"
        },
        "answer": {
            "a": "wine",
            "b": "won",
            "c": "when",
            "d": "wean",
            "correct": "a",
            "swedish": "wine"
        }
    },
    {
        "question": {
            "swedish": "vatten",
            "english": "water"
        },
        "answer": {
            "a": "vetting",
            "b": "water",
            "c": "comprehension",
            "d": "veteran",
            "correct": "b",
            "swedish": "vatten"
        }
    },
    {
        "question": {
            "swedish": "biff",
            "english": "beef"
        },
        "answer": {
            "a": "bark",
            "b": "fight",
            "c": "beef",
            "d": "puff",
            "correct": "c",
            "swedish": "biff"
        }
    },
    {
        "question": {
            "swedish": "fläsk",
            "english": "pork"
        },
        "answer": {
            "a": "flask",
            "b": "bottle",
            "c": "steak",
            "d": "pork",
            "correct": "d",
            "swedish": "fläsk"
        }
    },
    {
        "question": {
            "swedish": "kyckling",
            "english": "chicken"
        },
        "answer": {
            "a": "chicken",
            "b": "cackling",
            "c": "chuckling",
            "d": "heckling",
            "correct": "a",
            "swedish": "kyckling"
        }
    },
    {
        "question": {
            "swedish": "lamm",
            "english": "lamb"
        },
        "answer": {
            "a": "car",
            "b": "lamb",
            "c": "limb",
            "d": "talk",
            "correct": "b",
            "swedish": "lamm"
        }
    },
    {
        "question": {
            "swedish": "fisk",
            "english": "fish"
        },
        "answer": {
            "a": "fuss",
            "b": "fist",
            "c": "fish",
            "d": "fake",
            "correct": "c",
            "swedish": "fisk"
        }
    },
    {
        "question": {
            "swedish": "fot",
            "english": "foot"
        },
        "answer": {
            "a": "faux",
            "b": "fee",
            "c": "though",
            "d": "foot",
            "correct": "d",
            "swedish": "fot"
        }
    },
    {
        "question": {
            "swedish": "ben",
            "english": "leg"
        },
        "answer": {
            "a": "leg",
            "b": "son",
            "c": "bin",
            "d": "bun",
            "correct": "a",
            "swedish": "ben"
        }
    },
    {
        "question": {
            "swedish": "huvud",
            "english": "head"
        },
        "answer": {
            "a": "halved",
            "b": "head",
            "c": "hand",
            "d": "divide",
            "correct": "b",
            "swedish": "huvud"
        }
    },
    {
        "question": {
            "swedish": "mun",
            "english": "mouth"
        },
        "answer": {
            "a": "man",
            "b": "mum",
            "c": "mouth",
            "d": "moon",
            "correct": "c",
            "swedish": "mun"
        }
    },
    {
        "question": {
            "swedish": "näsa",
            "english": "nose"
        },
        "answer": {
            "a": "read",
            "b": "knowing",
            "c": "nigh",
            "d": "nose",
            "correct": "d",
            "swedish": "näsa"
        }
    },
    {
        "question": {
            "swedish": "öga",
            "english": "eye"
        },
        "answer": {
            "a": "eye",
            "b": "egg",
            "c": "examine",
            "d": "chew",
            "correct": "a",
            "swedish": "eye"
        }
    },
    {
        "question": {
            "swedish": "kropp",
            "english": "body"
        },
        "answer": {
            "a": "militia",
            "b": "body",
            "c": "cow",
            "d": "key",
            "correct": "b",
            "swedish": "kropp"
        }
    },
    {
        "question": {
            "swedish": "mage",
            "english": "stomach"
        },
        "answer": {
            "a": "image",
            "b": "mug",
            "c": "stomach",
            "d": "foot",
            "correct": "c",
            "swedish": "mage"
        }
    },
    {
        "question": {
            "swedish": "rygg",
            "english": "back"
        },
        "answer": {
            "a": "rye",
            "b": "shoulder",
            "c": "rug",
            "d": "back",
            "correct": "d",
            "swedish": "rygg"
        }
    },
    {
        "question": {
            "swedish": "chef",
            "english": "boss"
        },
        "answer": {
            "a": "boss",
            "b": "cheif",
            "c": "chef",
            "d": "composer",
            "correct": "a",
            "swedish": "chef"
        }
    },
    {
        "question": {
            "swedish": "sjuksköterska",
            "english": "nurse"
        },
        "answer": {
            "a": "water ski",
            "b": "nurse",
            "c": "ham sandwich",
            "d": "pediatrician",
            "correct": "b",
            "swedish": "sjuksköterska"
        }
    },
    {
        "question": {
            "swedish": "läkare",
            "english": "doctor"
        },
        "answer": {
            "a": "locker",
            "b": "basement",
            "c": "doctor",
            "d": "delicious",
            "correct": "c",
            "swedish": "läkare"
        }
    },
    {
        "question": {
            "swedish": "poliskonstapel",
            "english": "police officer"
        },
        "answer": {
            "a": "mayor",
            "b": "school nurse",
            "c": "police station",
            "d": "police officer",
            "correct": "d",
            "swedish": "poliskonstapel"
        }
    },
    {
        "question": {
            "swedish": "kock",
            "english": "(a) cook/chef"
        },
        "answer": {
            "a": "(a) cook/chef",
            "b": "soup",
            "c": "barbeque",
            "d": "a meal",
            "correct": "a",
            "swedish": "kock"
        }
    },
    {
        "question": {
            "swedish": "ingenjör",
            "english": "engineer"
        },
        "answer": {
            "a": "encounter",
            "b": "engineer",
            "c": "integer",
            "d": "uninjured",
            "correct": "b",
            "swedish": "ingenjör"
        }
    },
    {
        "question": {
            "swedish": "lärare",
            "english": "teacher"
        },
        "answer": {
            "a": "learner",
            "b": "lawyer",
            "c": "teacher",
            "d": "professor",
            "correct": "c",
            "swedish": "lärare"
        }
    },
    {
        "question": {
            "swedish": "programmerare",
            "english": "programmer"
        },
        "answer": {
            "a": "programming",
            "b": "documentation",
            "c": "organiser",
            "d": "programmer",
            "correct": "d",
            "swedish": "programmerare"
        }
    },
    {
        "question": {
            "swedish": "snickare",
            "english": "carpenter"
        },
        "answer": {
            "a": "carpenter",
            "b": "gossiper",
            "c": "laughter",
            "d": "snickers",
            "correct": "a",
            "swedish": "eye"
        }
    },
    {
        "question": {
            "swedish": "försäljare",
            "english": "salesman"
        },
        "answer": {
            "a": "frolicker",
            "b": "salesman",
            "c": "freeloader",
            "d": "tour guide",
            "correct": "b",
            "swedish": "försäljare"
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
