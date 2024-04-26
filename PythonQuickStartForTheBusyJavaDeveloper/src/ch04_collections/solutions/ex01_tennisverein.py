mitglieder_liste = []
mitglieder_liste += [ "Michael", "Tim", "Werner" ]

print(mitglieder_liste)

print("Jana?", "Jana" in mitglieder_liste)

mitglieder_liste.append("Andreas")
print(mitglieder_liste)

mitglieder_liste.extend(["Lili", "Jana", "Natalija"])
print(mitglieder_liste)

print(len(mitglieder_liste))
