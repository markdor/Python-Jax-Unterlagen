print("##################################################################")
print("NESTED SETS")
print("##################################################################")

colors = {"RED", "GREEN", "BLUE"}
print(colors)

# ADD SET TO SET:
try:
    colors.add({"PINK", "PURPLE"})
    print(colors)
except TypeError as ex:
    print("!!!!!!!!!!!!!! TypeError:", ex)

# ABHILFE: frozenset
frozen = frozenset({"PINK", "PURPLE"})
print(frozen)
print(set(frozen))

# ADD FROZEN SET TO SET
colors.add(frozenset({"PINK", "PURPLE"}))
print(colors)


print("##################################################################")
print("NESTED DICT")
print("##################################################################")

names_contacts = {"PETER": {"HOME": "Zürich",
                            "DELIVERY": "RAPPI",
                            "TECHNOLOGY": "JAVA"},
                  "MICHA": {"HOME": "Zürich",
                            "DELIVERY": "RAPPI",
                            "TECHNOLOGY": ["JAVA", "PYTHON"]}}
print(names_contacts)

#### WHY ? :-) => JUST THE KEY :-)
try:
    bad_nesting = {{"KEY": "K1"}: {"HOME": "Zürich"},
                   {"KEY": "K2"}: {"HOME": "Rapperswil"}}
    print(bad_nesting)
except TypeError as ex:
    print("!!!!!!!!!!!!!! TypeError:", ex)

# WHAT ABOUT frozenDIct => pip install frozendict
import frozendict

dict_key_nesting = {frozendict.frozendict({"KEY": "K1"}): {"HOME": "Zürich"},
                    frozendict.frozendict({"KEY": "K2"}): {"HOME": "Rapperswil"}}
print(dict_key_nesting)

# Alternative, wenn nur 1 KV-Pair: Tuple

dict_key_nesting = {("KEY", "K1"): {"HOME": "Zürich"},
                    ("KEY", "K2"): {"HOME": "Rapperswil"}}
print(dict_key_nesting)


print("##################################################################")
print("JSON DICT")
print("##################################################################")

json = {
    "country": "CH",
    "cities": [
        {
            "cityname": "Zürich",
            "postcode": 8047,
        },
        {
            "cityname": "Rapperswil",
            "postcode": 8640,
        }
    ],
    "country": "Switzerland",
    "capitalcity": "Bern",
    "state": "Bern",
}
print(json)
