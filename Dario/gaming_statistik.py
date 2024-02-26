def durchschnittliche_punkte_berechnen(punkte, spiele):
    return punkte / spiele


def benutzer_interaktion():
    try:
        punkte = int(input("Gib die gesammelten Punkte ein: "))
        spiele = int(input("Gib die Anzahl der Spiele ein: "))
    except ValueError:
        print("Ungültige Eingabe. Bitte gib eine Zahl ein.")
        return
    try:
        ergebnis = durchschnittliche_punkte_berechnen(punkte, spiele)
    except Exception as e:
        print("Fehler:", e)
        return
    if spiele == 0:
        print("Du hast keine Spiele gespielt.")
        return
    print("Der Durchschnitt beträgt", ergebnis)
    benutzer_interaktion()



benutzer_interaktion()
