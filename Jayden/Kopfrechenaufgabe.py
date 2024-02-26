versuch = 1
versuche = 4
ergebnis = 15
print("Berechne diese Aufgabe im Kopf: \n5 * 2 + 10 - 5 = x")

for versuch in range(1,5):
    x = int(input())
    if x == ergebnis:
        print(f"Glückwunsch, du hast es in {versuch} Versuchen geschafft")
        break
    else:
        versuche -= 1
        print(f"Das war falsch, du hast noch {versuche}")
        versuch + 1
        