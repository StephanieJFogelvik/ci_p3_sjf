import random
import time

# 100 basic Swedish words and phrases, with possible answers:
quiz_answers = [
    {
        "question": {
            "swedish": "VECKA",
            "english": "WEEK"
        },
        "answer": {
            "a": "VALLEY",
            "b": "WIGGLE",
            "c": "WEEK",
            "d": "TRAVEL",
            "correct": "c",
            "swedish": "VECKA"
        }
    },
    {
        "question": {
            "swedish": "ÅR",
            "english": "YEAR"
        },
        "answer": {
            "a": "OAR",
            "b": "ORE",
            "c": "OR",
            "d": "YEAR",
            "correct": "d",
            "swedish": "ÅR"
        }
    },
    {
        "question": {
            "swedish": "IDAG",
            "english": "TODAY"
        },
        "answer": {
            "a": "DOG",
            "b": "COD",
            "c": "TODAY",
            "d": "DAY",
            "correct": "c",
            "swedish": "IDAG"
        }
    },
    {
        "question": {
            "swedish": "IMORGON",
            "english": "TOMORROW"
        },
        "answer": {
            "a": "AIR GUN",
            "b": "ORGAN",
            "c": "TOMORROW",
            "d": "MIRROR",
            "correct": "c",
            "swedish": "IMORGON"
        }
    },
    {
        "question": {
            "swedish": "IGÅR",
            "english": "YESTERDAY"
        },
        "answer": {
            "a": "EAGLE",
            "b": "YESTERDAY",
            "c": "OGRE",
            "d": "IGLOO",
            "correct": "b",
            "swedish": "IGÅR"
        }
    },
    {
        "question": {
            "swedish": "KALENDER",
            "english": "CALENDAR"
        },
        "answer": {
            "a": "CYLINDER",
            "b": "CALENDAR",
            "c": "COMMANDER",
            "d": "COLANDER",
            "correct": "b",
            "swedish": "KALENDER"
        }
    },
    {
        "question": {
            "swedish": "SEKUND",
            "english": "SECOND"
        },
        "answer": {
            "a": "SECOND",
            "b": "SUCCUMBED",
            "c": "TYPHOON",
            "d": "SICKENED",
            "correct": "a",
            "swedish": "SEKUND"
        }
    },
    {
        "question": {
            "swedish": "TIMME",
            "english": "HOUR"
        },
        "answer": {
            "a": "TONNE",
            "b": "HOUR",
            "c": "THIMBLE",
            "d": "TEEMING",
            "correct": "b",
            "swedish": "HOUR"
        }
    },
    {
        "question": {
            "swedish": "MINUT",
            "english": "MINUTE"
        },
        "answer": {
            "a": "SMALL",
            "b": "WELL",
            "c": "MINUTE",
            "d": "MAGNET",
            "correct": "c",
            "swedish": "MINUT"
        }
    },
    {
        "question": {
            "swedish": "KLOCKAN...",
            "english": "...O' CLOCK"
        },
        "answer": {
            "a": "KNOCKING",
            "b": "CLOCK IN",
            "c": "COOKING",
            "d": "...O' CLOCK",
            "correct": "d",
            "swedish": "KLOCKAN..."
        }
    },
    {
        "question": {
            "swedish": "KLOCKA",
            "english": "CLOCK"
        },
        "answer": {
            "a": "CLOAK",
            "b": "CLICK",
            "c": "CLOCK",
            "d": "CLOG",
            "correct": "c",
            "swedish": "kLOCKA"
        }
    },
    {
        "question": {
            "swedish": "EN TIMME",
            "english": "ONE HOUR"
        },
        "answer": {
            "a": "IN TIME",
            "b": "ENDING",
            "c": "ON TIME",
            "d": "ONE HOUR",
            "correct": "d",
            "swedish": "EN TIMME"
        }
    },
    {
        "question": {
            "swedish": "KAN",
            "english": "CAN"
        },
        "answer": {
            "a": "KIN",
            "b": "CON",
            "c": "CAN",
            "d": "BAN",
            "correct": "c",
            "swedish": "KAN"
        }
    },
    {
        "question": {
            "swedish": "ANVÄNDA",
            "english": "USE"
        },
        "answer": {
            "a": "INVADE",
            "b": "USE",
            "c": "ANTENNAE",
            "d": "ENVIED",
            "correct": "b",
            "swedish": "ANVÄNDA"
        }
    },
    {
        "question": {
            "swedish": "GÖRA",
            "english": "DO"
        },
        "answer": {
            "a": "GROW",
            "b": "DO",
            "c": "GREY",
            "d": "SEW",
            "correct": "b",
            "swedish": "GÖRA"
        }
    },
    {
        "question": {
            "swedish": "GÅ",
            "english": "GO"
        },
        "answer": {
            "a": "GO",
            "b": "SO",
            "c": "DO",
            "d": "EYE",
            "correct": "a",
            "swedish": "GÅ"
        }
    },
    {
        "question": {
            "swedish": "KOMMA",
            "english": "COME"
        },
        "answer": {
            "a": "COMMA",
            "b": "COMMON",
            "c": "CALMLY",
            "d": "COME",
            "correct": "d",
            "swedish": "KOMMA"
        }
    },
    {
        "question": {
            "swedish": "SKRATTA",
            "english": "LAUGH"
        },
        "answer": {
            "a": "SKIRT",
            "b": "SQUAT",
            "c": "LAUGH",
            "d": "RAKE",
            "correct": "c",
            "swedish": "SKRATTA"
        }
    },
    {
        "question": {
            "swedish": "SÄGA",
            "english": "SAY"
        },
        "answer": {
            "a": "THING",
            "b": "ROOF",
            "c": "SAY",
            "d": "WRITE",
            "correct": "c",
            "swedish": "SÄGA"
        }
    },
    {
        "question": {
            "swedish": "SE",
            "english": "SEE"
        },
        "answer": {
            "a": "SOOTHE",
            "b": "SEA",
            "c": "SEE",
            "d": "FEE",
            "correct": "c",
            "swedish": "SE"
        }
    },
    {
        "question": {
            "swedish": "LÅNGT",
            "english": "FAR"
        },
        "answer": {
            "a": "LIGHT",
            "b": "FAR",
            "c": "LEAD",
            "d": "NARROW",
            "correct": "b",
            "swedish": "LÅNGT"
        }
    },
    {
        "question": {
            "swedish": "LITEN",
            "english": "SMALL"
        },
        "answer": {
            "a": "LIGHTWEIGHT",
            "b": "BOTTLE",
            "c": "DOG",
            "d": "SMALL",
            "correct": "d",
            "swedish": "LITEN"
        }
    },
    {
        "question": {
            "swedish": "STOR",
            "english": "BIG"
        },
        "answer": {
            "a": "STEER",
            "b": "BIG",
            "c": "HOUSE",
            "d": "HORSE",
            "correct": "b",
            "swedish": "STOR"
        }
    },
    {
        "question": {
            "swedish": "VACKER",
            "english": "BEAUTIFUL"
        },
        "answer": {
            "a": "MIRROR",
            "b": "BEAUTIFUL",
            "c": "STAIRWELL",
            "d": "CEILING",
            "correct": "b",
            "swedish": "VACKER"
        }
    },
    {
        "question": {
            "swedish": "FUL",
            "english": "UGLY"
        },
        "answer": {
            "a": "FULL",
            "b": "PRETTY",
            "c": "BOTTLE",
            "d": "UGLY",
            "correct": "d",
            "swedish": "FUL"
        }
    },
    {
        "question": {
            "swedish": "SVÅR",
            "english": "DIFFICULT"
        },
        "answer": {
            "a": "HEAVY",
            "b": "DIFFICULT",
            "c": "SORE",
            "d": "SAD",
            "correct": "b",
            "swedish": "SVÅR"
        }
    },
    {
        "question": {
            "swedish": "LÄTT",
            "english": "EASY"
        },
        "answer": {
            "a": "BUTTER",
            "b": "EASY",
            "c": "TICKET",
            "d": "CLOUD",
            "correct": "b",
            "swedish": "LÄTT"
        }
    },
    {
        "question": {
            "swedish": "BRA",
            "english": "GOOD"
        },
        "answer": {
            "a": "GOOD",
            "b": "BROTHER",
            "c": "BREW",
            "d": "BOROUGH",
            "correct": "a",
            "swedish": "BRA"
        }
    },
    {
        "question": {
            "swedish": "DÅLIG",
            "english": "BAD"
        },
        "answer": {
            "a": "GOOD",
            "b": "RADIO",
            "c": "EXPENSIVE",
            "d": "BAD",
            "correct": "d",
            "swedish": "DÅLIG"
        }
    },
    {
        "question": {
            "swedish": "NÄRA",
            "english": "NEAR"
        },
        "answer": {
            "a": "NEAR",
            "b": "FAR",
            "c": "NERVE",
            "d": "KNOW",
            "correct": "a",
            "swedish": "NÄRA"
        }
    },
    {
        "question": {
            "swedish": "TREVLIGT ATT TRÄFFAS",
            "english": "NICE TO MEET YOU"
        },
        "answer": {
            "a": "PLEASE EXCUSE ME",
            "b": "NICE TO MEET YOU",
            "c": "THIS IS MY STOP",
            "d": "NICE WEATHER TODAY",
            "correct": "b",
            "swedish": "TREVLIGT ATT TRÄFFAS"
        }
    },
    {
        "question": {
            "swedish": "HEJ",
            "english": "HI"
        },
        "answer": {
            "a": "SOUP",
            "b": "HEDGE",
            "c": "WALL",
            "d": "HI",
            "correct": "d",
            "swedish": "HEJ"
        }
    },
    {
        "question": {
            "swedish": "GOD MORGON!",
            "english": "GOOD MORNING!"
        },
        "answer": {
            "a": "GOOD AFTERNOON!",
            "b": "GOOD DAY!",
            "c": "GOOD MORON!",
            "d": "GOOD MORNING!",
            "correct": "d",
            "swedish": "GOD MORGON!"
        }
    },
    {
        "question": {
            "swedish": "GODDAG",
            "english": "GOOD AFTERNOON"
        },
        "answer": {
            "a": "GOOD DOG",
            "b": "HOW GAUDY",
            "c": "GOOD AFTERNOON",
            "d": "GOOD NIGHT",
            "correct": "c",
            "swedish": "GODDAG"
        }
    },
    {
        "question": {
            "swedish": "GOD KVÄLL",
            "english": "GOOD EVENING"
        },
        "answer": {
            "a": "GOOD MORNING",
            "b": "GOOD JOB",
            "c": "GOOD DAY",
            "d": "GOOD EVENING",
            "correct": "d",
            "swedish": "GOD KVÄLL"
        }
    },
    {
        "question": {
            "swedish": "GODNATT",
            "english": "GOOD NIGHT"
        },
        "answer": {
            "a": "HELLO",
            "b": "GOOD DAY",
            "c": "BYE",
            "d": "GOOD NIGHT",
            "correct": "d",
            "swedish": "GODNATT"
        }
    },
    {
        "question": {
            "swedish": "HUR MÅR DU?",
            "english": "HOW ARE YOU?"
        },
        "answer": {
            "a": "HOW MANY [FOR YOU]?",
            "b": "WHAT IS THAT?",
            "c": "WHERE ARE WE?",
            "d": "HOW ARE YOU?",
            "correct": "d",
            "swedish": "HUR MÅR DU?"
        }
    },
    {
        "question": {
            "swedish": "TACK",
            "english": "THANKS"
        },
        "answer": {
            "a": "TAKE",
            "b": "TALK",
            "c": "STACK",
            "d": "THANKS",
            "correct": "d",
            "swedish": "TACK"
        }
    },
    {
        "question": {
            "swedish": "NEJ",
            "english": "NO"
        },
        "answer": {
            "a": "YES",
            "b": "NEIGH",
            "c": "SORRY",
            "d": "NO",
            "correct": "d",
            "swedish": "NEJ"
        }
    },
    {
        "question": {
            "swedish": "JAB ÄR...[__]",
            "english": "I AM...[NAME]"
        },
        "answer": {
            "a": "I AM..[__]",
            "b": "I WANT...[__]",
            "c": "I WENT TO...[__]",
            "d": "I SAW...[__]",
            "correct": "a",
            "swedish": "JAG ÄR...[__]"
        }
    },
    {
        "question": {
            "swedish": "HEJ DÅ",
            "english": "GOODBYE"
        },
        "answer": {
            "a": "HELLO",
            "b": "GOODBYE",
            "c": "TALLYHO",
            "d": "CHEERS",
            "correct": "b",
            "swedish": "HEJ DÅ"
        }
    },
    {
        "question": {
            "swedish": "JA",
            "english": "YES"
        },
        "answer": {
            "a": "YES",
            "b": "MAYBE",
            "c": "ELK",
            "d": "ROAR",
            "correct": "a",
            "swedish": "JA"
        }
    },
    {
        "question": {
            "swedish": "MÅNDAG",
            "english": "MONDAY"
        },
        "answer": {
            "a": "MAD DOG",
            "b": "MONDAY",
            "c": "MATTOCK",
            "d": "MAY DAY",
            "correct": "b",
            "swedish": "MÅNDAG"
        }
    },
    {
        "question": {
            "swedish": "TISDAG",
            "english": "TUESDAY"
        },
        "answer": {
            "a": "TODAY",
            "b": "TEDDY",
            "c": "TUESDAY",
            "d": "TOOTHY",
            "correct": "c",
            "swedish": "TISDAG"
        }
    },
    {
        "question": {
            "swedish": "ONSDAG",
            "english": "WEDNESDAY"
        },
        "answer": {
            "a": "TWENTY",
            "b": "WANDER",
            "c": "WHEEZY",
            "d": "WEDNESDAY",
            "correct": "d",
            "swedish": "ONSDAG"
        }
    },
    {
        "question": {
            "swedish": "TORSDAG",
            "english": "THURSDAY"
        },
        "answer": {
            "a": "THURSDAY",
            "b": "THIRD DAY",
            "c": "THREADY",
            "d": "THOROUGH",
            "correct": "a",
            "swedish": "TORSDAG"
        }
    },
    {
        "question": {
            "swedish": "FREDAG",
            "english": "FRIDAY"
        },
        "answer": {
            "a": "FLIGHTY",
            "b": "FRIDAY",
            "c": "FRIARY",
            "d": "FRIGHTFUL",
            "correct": "b",
            "swedish": "FREDAG"
        }
    },
    {
        "question": {
            "swedish": "LÖRDAG",
            "english": "SATURDAY"
        },
        "answer": {
            "a": "LOWER DECK",
            "b": "ARCTIC",
            "c": "LÖRDAG",
            "d": "BURDOCK",
            "correct": "c",
            "swedish": "LÖRDAG"
        }
    },
    {
        "question": {
            "swedish": "SÖNDAG",
            "english": "SUNDAY"
        },
        "answer": {
            "a": "SUNDOG",
            "b": "SNAKE",
            "c": "SANDBAG",
            "d": "SUNDAY",
            "correct": "d",
            "swedish": "SÖNDAG"
        }
    },
    {
        "question": {
            "swedish": "JANUARI",
            "english": "JANUARY"
        },
        "answer": {
            "a": "JANUARY",
            "b": "JANISSARY",
            "c": "ANNUARY",
            "d": "YEARBOOK",
            "correct": "a",
            "swedish": "JANUARI"
        }
    },
    {
        "question": {
            "swedish": "FEBRUARI",
            "english": "FEBRUARY"
        },
        "answer": {
            "a": "FIBULARE",
            "b": "FEBRUARY",
            "c": "FEVER",
            "d": "FIBBING",
            "correct": "b",
            "swedish": "FEBRUARI"
        }
    },
    {
        "question": {
            "swedish": "MARS",
            "english": "MARCH"
        },
        "answer": {
            "a": "MARE",
            "b": "MORSE",
            "c": "MARCH",
            "d": "WAR",
            "correct": "c",
            "swedish": "MARS"
        }
    },
    {
        "question": {
            "swedish": "APRIL",
            "english": "APRIL"
        },
        "answer": {
            "a": "APRON",
            "b": "OPAL",
            "c": "APPLE",
            "d": "APRIL",
            "correct": "d",
            "swedish": "APRIL"
        }
    },
    {
        "question": {
            "swedish": "MAJ",
            "english": "MAY"
        },
        "answer": {
            "a": "MAY",
            "b": "MATCH",
            "c": "MERGE",
            "d": "NUDGE",
            "correct": "a",
            "swedish": "MAJ"
        }
    },
    {
        "question": {
            "swedish": "JUNI",
            "english": "JUNE"
        },
        "answer": {
            "a": "UNI",
            "b": "JUNE",
            "c": "GOON",
            "d": "JOIN ME",
            "correct": "b",
            "swedish": "JUNI"
        }
    },
    {
        "question": {
            "swedish": "JULI",
            "english": "JULY"
        },
        "answer": {
            "a": "PRETTY",
            "b": "TANGERINE",
            "c": "JULY",
            "d": "A SMALL FISHING VESSEL",
            "correct": "c",
            "swedish": "JULI"
        }
    },
    {
        "question": {
            "swedish": "SEPTEMBER",
            "english": "SEPTEMBER"
        },
        "answer": {
            "a": "SEPTUM",
            "b": "TIMBER",
            "c": "FOUL-TEMPERED",
            "d": "SEPTEMBER",
            "correct": "d",
            "swedish": "SEPTEMBER"
        }
    },
    {
        "question": {
            "swedish": "NOVEMBER",
            "english": "NOVEMBER"
        },
        "answer": {
            "a": "NOVEMBER",
            "b": "NOVELTY",
            "c": "NOTORIOUS",
            "d": "NEVERMORE",
            "correct": "a",
            "swedish": "NOVEMBER"
        }
    },
    {
        "question": {
            "swedish": "DECEMBER",
            "english": "DECEMBER"
        },
        "answer": {
            "a": "CUCUMBER",
            "b": "DECEMBER",
            "c": "DISSEMBLE",
            "d": "DISHONOUR",
            "correct": "b",
            "swedish": "DECEMBER"
        }
    },
    {
        "question": {
            "swedish": "NOLL",
            "english": "ZERO"
        },
        "answer": {
            "a": "KNOLL",
            "b": "NILE",
            "c": "ZERO",
            "d": "KNEEL",
            "correct": "c",
            "swedish": "NOLL"
        }
    },
    {
        "question": {
            "swedish": "ETT",
            "english": "ONE"
        },
        "answer": {
            "a": "IT",
            "b": "OUT",
            "c": "WHEN",
            "d": "ONE",
            "correct": "d",
            "swedish": "ETT"
        }
    },
    {
        "question": {
            "swedish": "TVÅ",
            "english": "TWO"
        },
        "answer": {
            "a": "TWO",
            "b": "TEA",
            "c": "TEE",
            "d": "TOW",
            "correct": "a",
            "swedish": "TVÅ"
        }
    },
    {
        "question": {
            "swedish": "TRE",
            "english": "THREE"
        },
        "answer": {
            "a": "TRAY",
            "b": "THREE",
            "c": "TRUE",
            "d": "TREE",
            "correct": "b",
            "swedish": "THREE"
        }
    },
    {
        "question": {
            "swedish": "FYRA",
            "english": "FOUR"
        },
        "answer": {
            "a": "FIERY",
            "b": "FERRY",
            "c": "FOUR",
            "d": "FREE",
            "correct": "c",
            "swedish": "FYRA"
        }
    },
    {
        "question": {
            "swedish": "FEM",
            "english": "FIVE"
        },
        "answer": {
            "a": "FEMME",
            "b": "FOAM",
            "c": "FAWN",
            "d": "FIVE",
            "correct": "d",
            "swedish": "FEM"
        }
    },
    {
        "question": {
            "swedish": "SEX",
            "english": "SIX"
        },
        "answer": {
            "a": "SIX",
            "b": "SOCKS",
            "c": "SAX",
            "d": "SECTS",
            "correct": "a",
            "swedish": "SEX"
        }
    },
    {
        "question": {
            "swedish": "SJU",
            "english": "SEVEN"
        },
        "answer": {
            "a": "SIGH",
            "b": "SEVEN",
            "c": "FLU",
            "d": "SEW",
            "correct": "b",
            "swedish": "SJU"
        }
    },
    {
        "question": {
            "swedish": "ÅTTA",
            "english": "EIGHT"
        },
        "answer": {
            "a": "TWO",
            "b": "UNDERSTAND",
            "c": "EIGHT",
            "d": "TIE",
            "correct": "c",
            "swedish": "ÅTTA"
        }
    },
    {
        "question": {
            "swedish": "NIO",
            "english": "NINE"
        },
        "answer": {
            "a": "NEO",
            "b": "HAPPY",
            "c": "MEOW",
            "d": "NINE",
            "correct": "d",
            "swedish": "NIO"
        }
    },
    {
        "question": {
            "swedish": "TIO",
            "english": "TEN"
        },
        "answer": {
            "a": "TEN",
            "b": "TIE",
            "c": "TILE",
            "d": "THAW",
            "correct": "a",
            "swedish": "TIO"
        }
    },
    {
        "question": {
            "swedish": "KAFFE",
            "english": "COFFEE"
        },
        "answer": {
            "a": "COUGHING",
            "b": "COFFEE",
            "c": "CALF",
            "d": "GOOF",
            "correct": "b",
            "swedish": "KAFFE"
        }
    },
    {
        "question": {
            "swedish": "TÉ",
            "english": "TEA"
        },
        "answer": {
            "a": "THEE",
            "b": "TO",
            "c": "TEA",
            "d": "HE",
            "correct": "c",
            "swedish": "TEA"
        }
    },
    {
        "question": {
            "swedish": "ÖL",
            "english": "BEER"
        },
        "answer": {
            "a": "WOOL",
            "b": "ILL",
            "c": "OWL",
            "d": "BEER",
            "correct": "d",
            "swedish": "ÖL"
        }
    },
    {
        "question": {
            "swedish": "VIN",
            "english": "WINE"
        },
        "answer": {
            "a": "WINE",
            "b": "WON",
            "c": "WHEN",
            "d": "WEAN",
            "correct": "a",
            "swedish": "WINE"
        }
    },
    {
        "question": {
            "swedish": "VATTEN",
            "english": "WATER"
        },
        "answer": {
            "a": "VETTING",
            "b": "WATER",
            "c": "COMPREHENSION",
            "d": "VETERAN",
            "correct": "b",
            "swedish": "VATTEN"
        }
    },
    {
        "question": {
            "swedish": "BIFF",
            "english": "BEEF"
        },
        "answer": {
            "a": "BARK",
            "b": "FIGHT",
            "c": "BEEF",
            "d": "PUFF",
            "correct": "c",
            "swedish": "BIFF"
        }
    },
    {
        "question": {
            "swedish": "FLÄSK",
            "english": "PORK"
        },
        "answer": {
            "a": "FLASK",
            "b": "BOTTLE",
            "c": "STEAK",
            "d": "PORK",
            "correct": "d",
            "swedish": "FLÄSK"
        }
    },
    {
        "question": {
            "swedish": "KYCKLING",
            "english": "CHICKEN"
        },
        "answer": {
            "a": "CHICKEN",
            "b": "CACKLING",
            "c": "CHUCKLING",
            "d": "HECKLING",
            "correct": "a",
            "swedish": "KYCKLING"
        }
    },
    {
        "question": {
            "swedish": "LAMM",
            "english": "LAMB"
        },
        "answer": {
            "a": "CAR",
            "b": "LAMB",
            "c": "LIMB",
            "d": "TALK",
            "correct": "b",
            "swedish": "LAMM"
        }
    },
    {
        "question": {
            "swedish": "FISK",
            "english": "FISH"
        },
        "answer": {
            "a": "FUSS",
            "b": "FIST",
            "c": "FISH",
            "d": "FAKE",
            "correct": "c",
            "swedish": "FISK"
        }
    },
    {
        "question": {
            "swedish": "FOT",
            "english": "FOOT"
        },
        "answer": {
            "a": "FAUX",
            "b": "FEE",
            "c": "THOUGH",
            "d": "FOOT",
            "correct": "d",
            "swedish": "FOT"
        }
    },
    {
        "question": {
            "swedish": "BEN",
            "english": "LEG"
        },
        "answer": {
            "a": "LEG",
            "b": "SON",
            "c": "BIN",
            "d": "BUN",
            "correct": "a",
            "swedish": "BEN"
        }
    },
    {
        "question": {
            "swedish": "HUVUD",
            "english": "HEAD"
        },
        "answer": {
            "a": "HALVED",
            "b": "HEAD",
            "c": "HAND",
            "d": "DIVIDE",
            "correct": "b",
            "swedish": "HUVUD"
        }
    },
    {
        "question": {
            "swedish": "MUN",
            "english": "MOUTH"
        },
        "answer": {
            "a": "MAN",
            "b": "MUM",
            "c": "MOUTH",
            "d": "MOON",
            "correct": "c",
            "swedish": "MUN"
        }
    },
    {
        "question": {
            "swedish": "NÄSA",
            "english": "NOSE"
        },
        "answer": {
            "a": "READ",
            "b": "KNOWING",
            "c": "NIGH",
            "d": "NOSE",
            "correct": "d",
            "swedish": "NÄSA"
        }
    },
    {
        "question": {
            "swedish": "ÖGA",
            "english": "EYE"
        },
        "answer": {
            "a": "EYE",
            "b": "EGG",
            "c": "EXAMINE",
            "d": "CHEW",
            "correct": "a",
            "swedish": "EYE"
        }
    },
    {
        "question": {
            "swedish": "KROPP",
            "english": "BODY"
        },
        "answer": {
            "a": "MILITIA",
            "b": "BODY",
            "c": "COW",
            "d": "KEY",
            "correct": "b",
            "swedish": "KROPP"
        }
    },
    {
        "question": {
            "swedish": "MAGE",
            "english": "STOMACH"
        },
        "answer": {
            "a": "IMAGE",
            "b": "MUG",
            "c": "STOMACH",
            "d": "FOOT",
            "correct": "c",
            "swedish": "MAGE"
        }
    },
    {
        "question": {
            "swedish": "RYGG",
            "english": "BACK"
        },
        "answer": {
            "a": "RYE",
            "b": "SHOULDER",
            "c": "RUG",
            "d": "BACK",
            "correct": "d",
            "swedish": "RYGG"
        }
    },
    {
        "question": {
            "swedish": "CHEF",
            "english": "BOSS"
        },
        "answer": {
            "a": "BOSS",
            "b": "CHIEF",
            "c": "CHEF",
            "d": "COMPOSER",
            "correct": "a",
            "swedish": "CHEF"
        }
    },
    {
        "question": {
            "swedish": "SJUKSKÖTERSKA",
            "english": "NURSE"
        },
        "answer": {
            "a": "WATER SKI",
            "b": "NURSE",
            "c": "HAM SANDWICH",
            "d": "PEDIATRICIAN",
            "correct": "b",
            "swedish": "SJUKSKÖTERSKA"
        }
    },
    {
        "question": {
            "swedish": "LÄKARE",
            "english": "DOCTOR"
        },
        "answer": {
            "a": "LOCKER",
            "b": "BASEMENT",
            "c": "DOCTOR",
            "d": "DELICIOUS",
            "correct": "c",
            "swedish": "LÄKARE"
        }
    },
    {
        "question": {
            "swedish": "POLISKONSTAPEL",
            "english": "POLICE OFFICER"
        },
        "answer": {
            "a": "MAYOR",
            "b": "SCHOOL NURSE",
            "c": "POLICE STATION",
            "d": "POLICE OFFICER",
            "correct": "d",
            "swedish": "POLISKONSTAPEL"
        }
    },
    {
        "question": {
            "swedish": "KOCK",
            "english": "COOK/CHEF"
        },
        "answer": {
            "a": "COOK/CHEF",
            "b": "SOUP",
            "c": "BARBEQUE",
            "d": "A MEAL",
            "correct": "a",
            "swedish": "KOCK"
        }
    },
    {
        "question": {
            "swedish": "INGENJÖR",
            "english": "ENGINEER"
        },
        "answer": {
            "a": "ENCOUNTER",
            "b": "ENGINEER",
            "c": "INTEGER",
            "d": "UNINJURED",
            "correct": "b",
            "swedish": "INGENJÖR"
        }
    },
    {
        "question": {
            "swedish": "LÄRARE",
            "english": "TEACHER"
        },
        "answer": {
            "a": "LEARNER",
            "b": "LAWYER",
            "c": "TEACHER",
            "d": "PROFESSOR",
            "correct": "c",
            "swedish": "LÄRARE"
        }
    },
    {
        "question": {
            "swedish": "PROGRAMMERARE",
            "english": "PROGRAMMER"
        },
        "answer": {
            "a": "PROGRAMMING",
            "b": "DOCUMENTATION",
            "c": "ORGANISER",
            "d": "PROGRAMMER",
            "correct": "d",
            "swedish": "PROGRAMMERARE"
        }
    },
    {
        "question": {
            "swedish": "SNICKARE",
            "english": "CARPENTER"
        },
        "answer": {
            "a": "CARPENTER",
            "b": "GOSSIPER",
            "c": "LAUGHTER",
            "d": "SNICKERS",
            "correct": "a",
            "swedish": "SNICKARE"
        }
    },
    {
        "question": {
            "swedish": "FÖRSÄLJARE",
            "english": "SALESMAN"
        },
        "answer": {
            "a": "FROLICKER",
            "b": "SALESMAN",
            "c": "FREELOADER",
            "d": "TOUR GUIDE",
            "correct": "b",
            "swedish": "FÖRSÄLJARE"
        }
    }
]


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
print(2 * "\n")
flag()


# displays random flashcards for 3 seconds:
card_sets = []
print("LET'S PRACTICE SOME SWEDISH VOCABULARY!")
print(2 * "\n")
i = 1
while i < 6:
    random_number = random.randint(0, len(quiz_answers)-1)
    if quiz_answers[random_number] not in card_sets:
        card_sets.append(quiz_answers[random_number])
        i += 1


# quiz section:
print("QUIZ!")
print("")
questions = [card["question"] for card in card_sets]
answers = [card["answer"] for card in card_sets]

# prints out the question to the user:
for question in questions:
    print(f'Swedish: {question["swedish"]}, \
        English: {question["english"]}')
    print(2 * "\n")
    time.sleep(3)    # puts a 3 sec pause between questions:
# input from the user to trigger multiple choice based on the quiz above:
print("Press Enter")
input()

# Swe-flag image here (to push the flashcards out of view)
flag()

# Multiple choice questions:
SCORE = 0
for answer in answers:
    print(f'What is the English word for: {answer["swedish"]}?')
    print('Enter a letter for the correct answer (a, b, c, or d).')
    print(f' Is it A: {answer["a"]}, B: {answer["b"]}, C: {answer["c"]},\
        or D: {answer["d"]}?')
    user_input = input().lower()
    if user_input == answer["correct"]:
        print("")
        print("That is correct!")
        SCORE += 1
        print(2 * "\n")
    else:
        print("")
        print("Sorry! Wrong answer.")
        SCORE -= 1
        print(2 * "\n")
print("Your score: ")
print(SCORE)
print(5 * "\n")

print("Play again? Enter y for yes, n for no.")
input()
last_input = str(input)
for i in last_input:
    if last_input == "y":
        os.execv(sys.argv[0], sys.argv)       # 
    elif last_input == "n":
        break     # game ends here
    else:
        print('Please enter either "y" or "n"')
