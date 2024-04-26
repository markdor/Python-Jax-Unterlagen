# "Werte einer Tabelle"
values = [["Micha", 50, 8047, "Zürich"],
          ["Lili", 42, 8047, "Zürich"],
          ["Micha", 50, 52070, "Aachen"],
          ["Tim", 50, 24107, "Kiel"],
          ["Micha", 50, 24106, "Kiel"],
          ["Michael", 50, 24106, "Kiel"],
          ["Andreas", 50, 21012, "Hamburg"],
          ["Barbara", 48, 22395, "Hamburg"],
          ["Marianne", 83, 28816, "Stuhr"]]


values.sort(key=lambda p: (-p[1], p[0]))
print("Absteigend nach Alter und aufsteigend nach Name\n", values)


values.sort(key=lambda p: (p[3], -p[2]))
print("Nach Stadt, absteigend PLZ\n", values)


def by_city_and_zip_code_desc(p):
    return (p[3], -p[2])


values.sort(key=by_city_and_zip_code_desc)
print("Nach Stadt, absteigend PLZ\n", values)


values.sort(key=lambda p: (p[3], -p[2], p[0]))
print("Nach Stadt, absteigend PLZ, aufsteigend Name\n", values)