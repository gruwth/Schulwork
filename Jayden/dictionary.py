# Wörterbuch erstellen
personen = {}

# Namen und Alter hinzufügen
for _ in range(3):
    name = input("Bitte gib den Namen einer Person ein: ")
    alter = int(input(f"Bitte gib das Alter von {name} ein: "))
    personen[name] = alter

# Namen und Alter anzeigen
print("Namen und Alter aller Personen:")
for name, alter in personen.items():
    print(f"{name}: {alter}")

# Alter aktualisieren
name = input("Bitte gib den Namen einer Person ein, deren Alter aktualisiert werden soll: ")
if name in personen:
    neues_alter = int(input(f"Bitte gib das neue Alter von {name} ein: "))
    personen[name] = neues_alter
    print(f"Das Alter von {name} wurde aktualisiert.")
else:
    print(f"Die Person {name} existiert nicht im Wörterbuch.")

# Person entfernen
name = input("Bitte gib den Namen einer Person ein, die aus dem Wörterbuch entfernt werden soll: ")
if name in personen:
    personen.pop(name)
    print(f"{name} wurde aus dem Wörterbuch entfernt. Neues Wörterbuch: {personen}")
else:
    print(f"Die Person {name} existiert nicht im Wörterbuch.")