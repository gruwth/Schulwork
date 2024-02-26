def namenseingabe():
    names = []
    for i in range(5):
        name = input("Bitte gib den Namen der {}-ten Person ein: ".format(i+1))
        names.append(name)
    return names

def liste_ausgeben(names):
    reversed_names = names[::-1]
    print("Die Liste der Namen in umgekehrter Reihenfolge lautet: {}".format(reversed_names))

def neuen_namen_hinzufuegen(names):
    new_name = input("Bitte gib einen neuen Namen ein, der hinzugefügt werden soll: ")
    names.append(new_name)

def namen_ueberpruefen(names):
    name_to_check = input("Bitte gib einen Namen ein, um zu überprüfen, ob er in der Liste enthalten ist: ")
    if name_to_check in names:
        print("{} ist in der Liste enthalten.".format(name_to_check))
    else:
        print("{} ist nicht in der Liste enthalten.".format(name_to_check))

# Hauptprogramm
names = namenseingabe()
liste_ausgeben(names)
neuen_namen_hinzufuegen(names)
namen_ueberpruefen(names)