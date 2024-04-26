names = ["Tim", "Tom", "Mike", "Jim", "Tim", "Mike", "James", "Mike"]

name_to_count_map = {}

for name in names:
    if name not in name_to_count_map:
        name_to_count_map[name] = 1
    else:
        name_to_count_map[name] += 1

print(name_to_count_map)
