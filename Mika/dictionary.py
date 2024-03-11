class Dictionary:
    def __init__(self):
        self.personen = {}

    def add_person(self, name, alter):
        self.personen[name] = alter

    def display_persons(self):
        print("Namen und Alter aller Personen:")
        for name, alter in self.personen.items():
            print(f"{name}: {alter}")

    def update_age(self, name, neues_alter):
        if name in self.personen:
            self.personen[name] = neues_alter
            print(f"Das Alter von {name} wurde aktualisiert.")
        else:
            print(f"Die Person {name} existiert nicht im Wörterbuch.")

    def remove_person(self, name):
        if name in self.personen:
            self.personen.pop(name)
            print(f"{name} wurde aus dem Wörterbuch entfernt. Neues Wörterbuch: {self.personen}")
        else:
            print(f"Die Person {name} existiert nicht im Wörterbuch.")

# Usage example:
dictionary = Dictionary()

for _ in range(3):
    name = input("Bitte gib den Namen einer Person ein: ")
    alter = int(input(f"Bitte gib das Alter von {name} ein: "))
    dictionary.add_person(name, alter)

dictionary.display_persons()

name = input("Bitte gib den Namen einer Person ein, deren Alter aktualisiert werden soll: ")
if name in dictionary.personen:
    neues_alter = int(input(f"Bitte gib das neue Alter von {name} ein: "))
    dictionary.update_age(name, neues_alter)
else:
    print(f"Die Person {name} existiert nicht im Wörterbuch.")

name = input("Bitte gib den Namen einer Person ein, die aus dem Wörterbuch entfernt werden soll: ")
dictionary.remove_person(name)
 