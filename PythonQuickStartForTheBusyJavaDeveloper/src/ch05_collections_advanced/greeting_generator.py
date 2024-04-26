def greet_generator():
    yield "Hallo"
    yield "Hello"
    yield "Moin"
    yield "Grüezi"


greetings = greet_generator()
print(next(greetings))
print(next(greetings))
print(next(greetings))
print(next(greetings))

for greet in greet_generator():
    print(greet)
