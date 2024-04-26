names = []

names.append("Tim")
names.append("Tom")
print(names)

names.insert(0, "Anton")
names.insert(0, "Andreas")
print(names)

names.insert(4, "Last")
print(names)

names[1] = "Mike"
print(names)

#######################################

del names[2]
print(names)

names.remove("Tom")
print(names)

names.clear()
print(names)

names.remove("Tim")
print(names)
