def durchschnittliche_punkte_berechnen(gesamtpunktzahl, anzahl_spiele):
    if anzahl_spiele == 0:
        return 0
    elif anzahl_spiele > 0:
        return gesamtpunktzahl / anzahl_spiele
    else:
        raise ValueError("Die Anzahl der gespielten Spiele darf nicht negativ sein.")

def benutzerInteraktion():
    gesamtpunktzahl = int(input("Geben Sie die Gesamtpunktzahl ein: "))
    anzahl_spiele = int(input("Geben Sie die Anzahl der gespielten Spiele ein: "))

    durchschnittliche_punkte = durchschnittliche_punkte_berechnen(gesamtpunktzahl, anzahl_spiele)
    print("Die durchschnittliche Punktzahl pro Spiel beträgt:", durchschnittliche_punkte)

benutzerInteraktion()