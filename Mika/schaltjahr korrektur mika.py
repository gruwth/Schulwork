schaltjahr = False
jahr = int(input("Geben Sie ein Jahr ein: "))
if jahr % 4 == 0 and jahr % 100 != 0 or jahr % 400 == 0:
    schaltjahr = True

monat = int(input("Geben Sie ein Monat ein: "))
if monat == 2 and schaltjahr == True:
    tage = [j for j in range(1,30)]
elif monat == 2 and schaltjahr == False:
    tage = [j for j in range(1,29)]
else:
    i = [1,3,5,7,8,10,12]
    if monat in i:
        tage = [j for j in range(1,32)]
    else:
        tage = [j for j in range(1,31)]

tag = int(input("Geben Sie ein Tag ein: "))
if tag in tage:
    if schaltjahr is True:
        print(f"Das Datum existiert und {jahr} ist ein Schaltjahr")
    else:
        print(f"Das Datum existiert und {jahr} ist kein Schaltjahr")
else:
    print("Das Datum gibt es nicht")