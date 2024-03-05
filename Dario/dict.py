class PersonManager():
    def __init__(self):
        self.personen = {}
    
    def add_person(self, anzahl: int):
        for _ in range(anzahl):
            name = input("Bitte gib den Namen einer Person ein: ")
            alter = int(input(f"Bitte gib das Alter von {name} ein: "))
            person = Person(name, alter)
            self.personen[name] = person

    def show_personen(self):
        print("Namen und Alter aller Personen:")
        for _, person in self.personen.items():
            print(f"{person.name}: {person.alter} Jahre alt")

    def update_personen(self):
        name = input("Gib einen Person zum anpassen ein: ")
        if name in self.personen:
            neues_alter = int(input(f"Gib das neue Alter von {name} ein: "))
            self.personen[name].alter = neues_alter
            print(f"Das Alter von {name} wurde aktualisiert.")
        else:
            print(f"Die Person {name} existiert nicht im Wörterbuch.")
    
    def delete_personen(self):
        name = input("Gib eine Person ein die entfernt werden soll: ")
        if name in self.personen:
            self.personen.pop(name)
            print(f"{name} wurde aus dem Wörterbuch entfernt.")
        else:
            print(f"Die Person {name} existiert nicht im Wörterbuch.")

class Person():
    def __init__(self, name: str, alter: int):
        self.name = name
        self.alter = alter


if __name__ == "__main__":
    anzahl = int(input("Wie viele Personen möchtest du hinzufügen? "))
    pm = PersonManager()
    pm.add_person(anzahl)
    while True:
        pm.show_personen()
        pm.update_personen()
        pm.show_personen()
        pm.delete_personen()