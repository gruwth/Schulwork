
personen = {}

def add_person(anzahl: int):
    for _ in range(anzahl):
        name = input("Bitte gib den Namen einer Person ein: ")
        alter = int(input(f"Bitte gib das Alter von {name} ein: "))
        personen[name] = alter

def show_personen():
    print("Namen und Alter aller Personen:")
    for name, alter in personen.items():
        print(f"{name}: {alter} Jahre alt")

def update_personen():
    name = input("Gib einen Person zum anpassen ein: ")
    if name in personen:
        neues_alter = int(input(f"Gib das neue Alter von {name} ein: "))
        personen[name] = neues_alter
        print(f"Das Alter von {name} wurde aktualisiert.")
    else:
        print(f"Die Person {name} existiert nicht im Wörterbuch.")

def delete_personen():
    name = input("Gib eine Person ein die entfernt werden soll: ")
    if name in personen:
        personen.pop(name)
        print(f"{name} wurde aus dem Wörterbuch entfernt.")
    else:
        print(f"Die Person {name} existiert nicht im Wörterbuch.")

if __name__ == "__main__":
    anzahl = int(input("Wie viele Personen möchtest du hinzufügen? "))
    add_person(anzahl)
    while True:
        show_personen()
        update_personen()
        show_personen()
        delete_personen()

    