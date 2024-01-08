# Aufgabe2
# a = 5
# Summe = 9
# Ausgbe ist 9

# Aufgabe 5
note = int(input())
try:
    match note:
        case 1:
            print('sehr gut')
        case 2:
            print('gut')
        case 3:
            print('befriedigend')
        case 4:
            print('ausreichend')
        case 5:
            print('mangelhaft')
        case 6:
            print('ungenügend')
        case _:
            print('Fehlermeldung')
except ValueError as e:
    print(e)
