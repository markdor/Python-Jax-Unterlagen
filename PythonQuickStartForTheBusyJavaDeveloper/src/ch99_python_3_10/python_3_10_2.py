def ide_full_name(short_name):
    match short_name:
        case "PyC":
            return "PyCharm"
        case "VSC":
            return "Visual Studio Code"
        case "ECL":
            return "Eclipse"
        case _:
            return "Not Supported"


print(ide_full_name("PyC"))
print(ide_full_name("ECL"))

#######################################################

def match_lists(input):
    match input:
        case [1, 2]:
            print('First option')
        case [1, 2, 3]:
            print('Second option')


match_lists([1, 2])
match_lists([1, 2, 3])
match_lists([1, 2, 3, 4])


# Unmatchhed => None
def match_lists_with_return(input):
    match input:
        case [1, 2]:
            return 'First option'
        case [1, 2, 3]:
            return 'Second option'


print(match_lists_with_return([1, 2]))
print(match_lists_with_return([1, 2, 3]))
print(match_lists_with_return([1, 2, 3, 4]))