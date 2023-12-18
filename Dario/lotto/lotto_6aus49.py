import random


def validate(lst):
    return len(lst) == len(set(lst))


def input_():
    choices = []
    for i in range(6):
        z = int(input(f"Zahl {i + 1} Bitte: "))
        choices.append(z)
        choices.sort()

    superzahl = int(input("Superzahl Bitte: "))

    return choices, superzahl


def get_winners():
    regular_numbers = [random.randint(1, 49) for i in range(6)]
    superzahl = random.randint(1, 10)
    return regular_numbers, superzahl


def play(lst_input, sz_input, winners, sz_winner):
    amount = 0
    for i in lst_input:
        if i in winners:
            amount += 1

    print(f"Du hast {amount} richtig und die Superzahl {('richtig' if sz_input == sz_winner else 'falsch')}.")
    print("Gewinnerzahlen:", *winners)
    print("Superzahl:", sz_winner)


while True:
    guess_input, szl_input = input_()
    winners_, szl_winner = get_winners()

    while not validate(guess_input):
        print("Ungültige Eingabe. Bitte nochmal Versuchen.")
        lst_input, sz_input = input_()

    while not validate(winners_):
        winners_, szl_winner = get_winners()
    winners_.sort()

    play(guess_input, szl_input, winners_, szl_winner)

    x = input("Nochmal spielen? (y/n)\n").lower()
    if x == "n":
        break
