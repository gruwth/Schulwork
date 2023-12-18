import random


def validate(lst):
    return len(lst) == len(set(lst))


def input_():
    choices = []
    for i in range(6):
        z = int(input(f"Zahl {i+1} Bitte: "))
        choices.append(z)
        choices.sort()
    
    superzahl = int(input("Superzahl Bitte: "))
    
    return choices, superzahl


def get_winners():
    regular_numbers = [random.randint(1, 49) for i in range(6)]
    superzahl = random.randint(1, 10) 
    return regular_numbers, superzahl


def play():
    lst_input, superzahl_input = input_()
    
    while not validate(lst_input):
        print("Ungültige Eingabe. Bitte nochmal Versuchen.")
        lst_input, superzahl_input = input_()
    
    winners, superzahl_winner = get_winners()
    while not validate(winners):
        winners, superzahl_winner = get_winners()
    
    amount = 0
    for i in lst_input:
        if i in winners:
            amount += 1
    
    winners.sort()
    print(f"Du hast {amount} richtig und die Superzahl {('richtig' if superzahl_input == superzahl_winner else 'falsch')}.")
    print("Gewinnerzahlen:", *winners)
    print("Superzahl:", superzahl_winner)


while True:
    play()
    x = input("Nochmal spielen? (y/n)\n").lower()
    if x == "n":
        break
        