def durchschnittliche_punkte_berechnen(gesamtpunktzahl, anzahl_spiele):
    if anzahl_spiele == 0:
        return 0
    else:
        return gesamtpunktzahl / anzahl_spiele

def benutzerInteraktion():
    gesamtpunktzahl = int(input("Geben Sie die Gesamtpunktzahl ein: "))
    anzahl_spiele = int(input("Geben Sie die Anzahl der gespielten Spiele ein: "))
    durchschnitt = durchschnittliche_punkte_berechnen(gesamtpunktzahl, anzahl_spiele)
    print("Die durchschnittliche Punktzahl pro Spiel beträgt:", durchschnitt)

benutzerInteraktion()


# Zu testende Szenarien und Randfälle
# Beim Testen dieses Programms sollten Sie verschiedene Szenarien und mögliche Randfälle berücksichtigen, um sicherzustellen, dass es korrekt funktioniert. Hier einige Beispiele:

# Normale Bedingungen: Positive Gesamtpunktzahl und positive Anzahl von Spielen.
# Keine Spiele gespielt: Die Anzahl der Spiele ist 0. Das Programm sollte sicherstellen, dass es nicht durch Null teilt und stattdessen angemessen reagiert, z.B. durch Zurückgeben von 0 oder Ausgeben einer spezifischen Nachricht.
# Negative Werte: Was passiert, wenn negative Werte für die Gesamtpunktzahl oder die Anzahl der Spiele eingegeben werden? Obwohl dies im realen Szenario vielleicht nicht sinnvoll ist, sollte das Programm darauf vorbereitet sein oder die Eingabe solcher Werte verhindern.
# Große Zahlen: Große Eingabewerte sollten korrekt gehandhabt werden, ohne dass es zu Überlauf- oder Präzisionsproblemen kommt.
# Nicht-numerische Eingaben: Das Programm sollte angemessen auf nicht-numerische Eingaben reagieren, z.B. durch Aufforderung zur erneuten Eingabe.
# Diese Tests helfen dabei, die Robustheit und Zuverlässigkeit Ihrer Implementierung zu gewährleisten.