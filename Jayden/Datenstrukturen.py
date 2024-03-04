def namenseingabe():
    names = []
    for i in range(5):
        name = input(f"Bitte gib den Namen der {i+1}-ten Person ein: ")
        names.append(name)
    return names

def liste_ausgeben(names):
    reversed_names = names[::-1]
    print(f"Die Liste der Namen in umgekehrter Reihenfolge lautet: {reversed_names}")

def neuen_namen_hinzufuegen(names):
    new_name = input("Bitte gib einen neuen Namen ein, der hinzugefügt werden soll: ")
    if new_name in names:
        print(f"{new_name} ist bereits in der Liste enthalten.")
        neuen_namen_hinzufuegen(names)
    else:
        names.append(new_name)

def namen_ueberpruefen(names):
    name_to_check = input("Bitte gib einen Namen ein, um zu überprüfen, ob er in der Liste enthalten ist: ")
    if name_to_check in names:
        print(f"{name_to_check} ist in der Liste enthalten.")
    else:
        print(f"{name_to_check} ist nicht in der Liste enthalten.")

def namen_sortieren(names):
    sorted_names = sorted(names)
    print(f"Die sortierte Liste der Namen lautet: {sorted_names}")

# Hauptprogramm
names = namenseingabe()
liste_ausgeben(names)
neuen_namen_hinzufuegen(names)
namen_ueberpruefen(names)
liste_ausgeben(names)
