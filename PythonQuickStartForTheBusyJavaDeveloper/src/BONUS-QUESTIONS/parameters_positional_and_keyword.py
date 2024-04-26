def greet(name, msg):
    print("Hello", name + ', ' + msg)


# 2 positional
greet("Peter", "Good evening!")
# 2 keyword
greet(name="Michael", msg="Good afternoon")
# 2 keyword arguments (out of order)
greet(msg="How do you do?", name="James")
# 1 positional, 1 keyword argument
greet("Mike", msg="Good Night")


def greet_with_default(name, msg="Good morning!"):
    print("Hello", name + ', ' + msg)


greet_with_default("Peter", "Good evening!")
greet_with_default(name="Michael")


###########################################################

def special_keyword_enforced(man1, *, man2):
    print(man1)
    print(man2)


# TypeError: special_keyword_enforced() takes 1 positional argument but 2 were given
# special_keyword_enforced('not', 'working')
special_keyword_enforced('works', man2='fine')
special_keyword_enforced(man1 = 'works', man2='fine')


# https://stackoverflow.com/questions/24735311/what-does-the-slash-mean-in-help-output
# https://www.quora.com/What-does-the-slash-in-the-parameter-list-of-a-function-mean-in-Python
# https://peps.python.org/pep-0570/
# https://realpython.com/lessons/positional-only-arguments/
def very_special(pos_only, /, pos_or_kw, *, kw_only):
    print(pos_only)
    print(pos_or_kw)
    print(kw_only)


# TypeError: very_special() takes 2 positional arguments but 3 were given
# very_special('works', 'fine', 'not')
very_special('works', 'fine', kw_only='1')
very_special('works', pos_or_kw='fine', kw_only='2')
# TypeError: very_special() got some positional-only arguments passed as keyword arguments: 'pos_only'
#very_special(pos_only='WRONG', pos_or_kw='fine', kw_only='2')


def pos_only(pos_only, /):
    pass


def kw_only(*, kw_only):
    pass
