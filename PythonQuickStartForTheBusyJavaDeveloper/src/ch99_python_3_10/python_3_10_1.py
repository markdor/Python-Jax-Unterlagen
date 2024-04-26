http_code = 201

if http_code == 200:
    print("OK")
elif http_code == 201:
    print("CREATED")
elif http_code == 404:
    print("NOT FOUND")
elif http_code == 418:
    print("I AM A TEAPOT")
else:
    print("UNMATCHED CODE")

http_code = 501
match http_code:
    case 200:
        print("OK")
    case 201:
        print("CREATED")
    case 404:
        print("NOT FOUND")
    case 418:
        print("I AM A TEAPOT")
    case _:
        print("UNMATCHED CODE")


def get_info(day):
    match day:
        case 'Monday':
            return "I don't like..."
        case 'Thursday' | 'Friday':
             return 'Nearly there!'
        case 'Saturday' | 'Sunday':
             return 'Weekend!!!'
        case _:
             return 'In Between...'

################################

values = (2,3,4)
match values:
    case [1,2,3,4]:
        print("4 in a row")
    case [1,2,3] | [2,3,4]:
        print("3 in a row")
    case [1,2,4] | [1,3,4]:
        print("3 but not connected")
    case _:
        print("SINGLE OR DOUBLE")


from enum import Enum, auto


class Gender(Enum):
    MALE = auto()
    FEMALE = auto()


def classify(person):
    match person:
        case (name, age, "male" | Gender.MALE):
            print(f"{name} is a man and {age} years old")
        case (name, age, "female" | Gender.FEMALE):
            print(f"{name} is a woman and {age} years old")
        case (name, _, gender) if gender is not None:
            print(f"no age specified: {name} is {gender}")
        case (name, age, _) if age is not None:
            print(f"no gender specified: {name} is {age} years old.")


classify(("Micha", 50, "male"))
classify(("Lili", 42, Gender.FEMALE))
classify(("NO GENDER", 42, None))
classify(("NO AGE", None, "ALL"))


###############################################################


