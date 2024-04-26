values = [3, 4, 5, 8, 9]
print(values)

# hinzufüpgen
values[:0] = [1, 2]
print(values)

values[5:5] = [6, 7]
print(values)

#####################################################################
# genaue Position
values[9:] = [10, 11]
print(values)

# von hinten ausgehend (relativ), aber Achtung, überschreibt Startpos
# bzw. kann nicht hinter das letzte Elemente zum einfügen gesetzt werden
#values[-1:] = [10, 11]
#print(values)

# Liste anfügen
#values += [12, 13]
#print(values)
#####################################################################

# löschen
values[4:7] = []
print(values)

values[1:-2] = []
print(values)