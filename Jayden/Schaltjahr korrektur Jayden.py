def pruefeJahr(jahr):
    if jahr % 4 == 0 and jahr % 100 != 0 or jahr % 400 == 0:
        return True
    else:
        return False

def pruefeMonat(monat, schaltjahr):
    if monat == 2 and schaltjahr:
        return list(range(1, 30))
    elif monat == 2 and not schaltjahr:
        return list(range(1, 29))
    elif monat in [1, 3, 5, 7, 8, 10, 12]:
        return list(range(1, 32))
    else:
        return list(range(1, 31))

def pruefeTag(tag, tage, schaltjahr, jahr):
    if tag in tage:
        if schaltjahr:
            return f"Das Datum existiert und {jahr} ist ein Schaltjahr"
        else:
            return f"Das Datum existiert und {jahr} ist kein Schaltjahr"
    else:
        return "Das Datum gibt es nicht"

jahr = int(input("Geben Sie ein Jahr ein: "))
schaltjahr = pruefeJahr(jahr)

monat = int(input("Geben Sie ein Monat ein: "))
tage = pruefeMonat(monat, schaltjahr)

tag = int(input("Geben Sie ein Tag ein: "))
ergebnis = pruefeTag(tag, tage, schaltjahr, jahr)
print(ergebnis)
