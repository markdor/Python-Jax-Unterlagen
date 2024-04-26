bestellmenge = 1_000
lkw_kapazitaet = 75

restmenge = bestellmenge % lkw_kapazitaet
anzahl_fahrten = bestellmenge // lkw_kapazitaet

if restmenge != 0:
    anzahl_fahrten += 1

print(anzahl_fahrten)