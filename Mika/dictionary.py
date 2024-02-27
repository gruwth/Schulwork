# Wörterbuch erstellen
personen = {}

# Namen und Alter hinzufügen
for _ in range(3):
    name = input("Bitte gib den Namen einer Person ein: ")
    alter = int(input("Bitte gib das Alter von {} ein: ".format(name)))
    personen[name] = alter

# Namen und Alter anzeigen
print("Namen und Alter aller Personen:")
for name, alter in personen.items():
    print("{}: {}".format(name, alter))

# Alter aktualisieren
name = input("Bitte gib den Namen einer Person ein, deren Alter aktualisiert werden soll: ")
if name in personen:
    neues_alter = int(input("Bitte gib das neue Alter von {} ein: ".format(name)))
    personen[name] = neues_alter
    print("Das Alter von {} wurde aktualisiert.".format(name))
else:
    print("Die Person {} existiert nicht im Wörterbuch.".format(name))

# Person entfernen
name = input("Bitte gib den Namen einer Person ein, die aus dem Wörterbuch entfernt werden soll: ")
if name in personen:
    personen.pop(name)
    print("{} wurde aus dem Wörterbuch entfernt. Neues Wörterbuch: {}".format(name, personen))
else:
    print("Die Person {} existiert nicht im Wörterbuch.".format(name))