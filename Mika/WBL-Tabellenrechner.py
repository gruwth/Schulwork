import termtables as tt

Nettolistenpreis = float(input("Bitte geben Sie den Nettolistenpreis ein: "))
Lieferantenrabatt = float(input("Bitte geben Sie den Lieferantenrabatt in Prozent ein: "))
Zieleinkaufspreis = Nettolistenpreis - (Nettolistenpreis * Lieferantenrabatt / 100)
Zieleinkaufspreis = round(Zieleinkaufspreis, 2)
print("Der Zieleinkaufspreis beträgt: ", Zieleinkaufspreis)

Lieferantenskonto = float(input("Bitte geben Sie das Lieferantenskonto in Prozent ein: "))
Bareinkaufspreis = Zieleinkaufspreis - (Zieleinkaufspreis * Lieferantenskonto / 100)
Bareinkaufspreis = round(Bareinkaufspreis, 2)
print("Der Bareinkaufspreis beträgt: ", Bareinkaufspreis)

Bezugskosten = Zieleinkaufspreis * 0.01
Bezugskosten = round(Bezugskosten, 2)
Bezugspreis = Bareinkaufspreis + Bezugskosten
Bezugspreis = round(Bezugspreis, 2)
print("Der Bezugspreis beträgt: ", Bezugspreis)

hkz = float(input("Bitte geben Sie die HKZ ein: "))
Selbstkosten = Bezugspreis + (Bezugspreis * hkz / 100)
Selbstkosten = round(Selbstkosten, 2)
print("Die Selbstkosten betragen: ", Selbstkosten)

Gewinnzuschlag = float(input("Bitte geben Sie den Gewinnzuschlag in Prozent ein: "))
Barverkaufspreis = Selbstkosten + (Selbstkosten * Gewinnzuschlag / 100)
Barverkaufspreis = round(Barverkaufspreis, 2)
print("Der Barverkaufspreis beträgt: ", Barverkaufspreis)

Kundenskonto = float(input("Bitte geben Sie das Kundenskonto in Prozent ein: "))
Zielverkaufspreis = Barverkaufspreis + (Barverkaufspreis * Kundenskonto / 100)
Zielverkaufspreis = round(Zielverkaufspreis, 2)
print("Der Zieleinkaufspreis beträgt: ", Zielverkaufspreis)

Kundenrabatt = float(input("Bitte geben Sie den Kundenrabatt in Prozent ein: "))
Listenverkaufspreis = Zieleinkaufspreis + (Zieleinkaufspreis * Kundenrabatt / 100)
Listenverkaufspreis = round(Listenverkaufspreis, 2)
print("Der Listenverkaufspreis beträgt: ", Listenverkaufspreis)

Ust = 19
Bruttoverkaufspreis = Listenverkaufspreis + (Listenverkaufspreis * Ust / 100)
Bruttoverkaufspreis = round(Bruttoverkaufspreis, 2)
print("Der Bruttoverkaufspreis beträgt: ", Bruttoverkaufspreis)

tt.print(
    [
        [f'{Nettolistenpreis}€ (100%)', '**Nettolistenpreis**', ''],
        [f'-{Nettolistenpreis * Lieferantenrabatt / 100}€ (-{Lieferantenrabatt}%)', '-Lieferantenrabatt', ''],
        [f'= {Zieleinkaufspreis}€ ({100 - Lieferantenrabatt}%)', '= Zieleinkaufspreis', f'{Zieleinkaufspreis}€ (100%)'],
        ['', '-Lieferantenskonto']
    ]
)