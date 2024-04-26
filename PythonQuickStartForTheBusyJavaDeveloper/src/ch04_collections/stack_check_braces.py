from src.ch04_collections.stack import Stack


def check_parentheses(input):
    # Ungerade Länge kann keine wohlgeformte Klammerung sein
    if len(input) % 2 != 0:
        return False

    opening_parentheses = Stack()

    for char in input:
        if is_opening_parenthesis(char):
            opening_parentheses.push(char)
        elif is_closing_parenthesis(char):
            if opening_parentheses.is_empty():
                # Schließende vor öffnender Klammer
                return False

            last_opening_parens = opening_parentheses.pop()
            if not is_matching_parenthesis_pair(last_opening_parens, char):
                # Unterschiedliche Klammerpaare
                return False
        else:
            # Ungültiges Zeichen
            return False

    return opening_parentheses.is_empty()


def is_opening_parenthesis(ch):
    return ch == '(' or ch == '[' or ch == '{'


def is_closing_parenthesis(ch):
    return ch in [")", "]", "}"]


def is_matching_parenthesis_pair(opening, closing):
    return (opening == '(' and closing == ')') or \
           (opening == '[' and closing == ']') or \
           (opening == '{' and closing == '}')


print(check_parentheses("()"))
print(check_parentheses("([{{}}])"))
print(check_parentheses("((})"))
print(check_parentheses("(})"))

