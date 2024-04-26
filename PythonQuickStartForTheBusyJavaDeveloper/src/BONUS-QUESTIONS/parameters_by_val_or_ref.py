# https://www.geeksforgeeks.org/pass-by-reference-vs-value-in-python/

# call by "value"

greeting = "Hello"


def change(greeting):
    greeting = "Hello Again"
    print("Inside Function:", greeting)


change(greeting)
print("Outside Function:", greeting)


def change2(greeting):
    greeting += "Hello Again"
    print("Inside Function:", greeting)


change2(greeting)
print("Outside Function:", greeting)


#########################
# call by "reference" => “Pass by Value” nor “Pass by Reference” but it is “Pass by Object Reference”.
def surprise(values):
    values.append([1, 2, 3, 4])
    values += [5, 6, 7]
    print("Values inside the function:", values)


mylist = [10, 20, 30]
surprise(mylist)
print("Values outside the function:", mylist)


def surprise_2(values):
    values = values + [1, 2, 3, 4]
    values += [5, 6, 7]
    print("Values inside the function:", values)


mylist = [10, 20, 30]
surprise_2(mylist)
print("Values outside the function:", mylist)