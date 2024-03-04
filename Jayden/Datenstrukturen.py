class Namenverwaltung:
    def __init__(self):
        self.names = []

    def namenseingabe(self):
        for i in range(5):
            name = input(f"Bitte gib den Namen der {i+1}-ten Person ein: ")
            self.names.append(name)

    def liste_ausgeben(self):
        reversed_names = self.names[::-1]
        print(f"Die Liste der Namen in umgekehrter Reihenfolge lautet: {reversed_names}")

    def neuen_namen_hinzufuegen(self):
        new_name = input("Bitte gib einen neuen Namen ein, der hinzugefügt werden soll: ")
        if new_name in self.names:
            print(f"{new_name} ist bereits in der Liste enthalten.")
            self.neuen_namen_hinzufuegen()
        else:
            self.names.append(new_name)

    def namen_ueberpruefen(self):
        name_to_check = input("Bitte gib einen Namen ein, um zu überprüfen, ob er in der Liste enthalten ist: ")
        if name_to_check in self.names:
            print(f"{name_to_check} ist in der Liste enthalten.")
        else:
            print(f"{name_to_check} ist nicht in der Liste enthalten.")

    def namen_sortieren(self):
        sorted_names = sorted(self.names)
        print(f"Die sortierte Liste der Namen lautet: {sorted_names}")


# Hauptprogramm
namenverwaltung = Namenverwaltung()
namenverwaltung.namenseingabe()
namenverwaltung.liste_ausgeben()
namenverwaltung.neuen_namen_hinzufuegen()
namenverwaltung.namen_ueberpruefen()
namenverwaltung.liste_ausgeben()
