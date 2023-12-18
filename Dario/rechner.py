import random

ranges = {"plus": (1, 200), "minus": (1, 200), "mal": (1, 20), "geteilt": (1, 20)}

def get_aufgaben(amount):
    lst = []
    for i in range(amount):
        random_op = random.choice(list(ranges.items()))
        key, value = random_op
        
        r1, r2 = random.randint(value[0], value[1]), random.randint(value[0], value[1])
        
        match key:
            case "plus":
                lst.append((f"{r1} + {r2}", r1, r2, "+"))
            case "minus":
                lst.append((f"{r1} - {r2}", r1, r2, "-"))
            case "mal":
                lst.append((f"{r1} * {r2}", r1, r2, "*"))
            case "geteilt":
                lst.append((f"{r1} / {r2}", r1, r2, "/"))
    return lst

def main():
    v = int(input("Wie viele Aufgaben möchtest du rechnen?\n"))
    aufgaben = get_aufgaben(v)

    for i in range(v):
        solution = 0

        match aufgaben[i][3]:
            case "+":
                solution = aufgaben[i][1] + aufgaben[i][2]
            case "-":
                solution = aufgaben[i][1] - aufgaben[i][2]
            case "*":
                solution = aufgaben[i][1] * aufgaben[i][2]
            case "/":
                solution = round(aufgaben[i][1] / aufgaben[i][2], 2)

        for attempt in range(3):
            try:
                g_input = float(input(f"Aufgabe: {aufgaben[i][0]}\nLösung (Versuch {attempt + 1}): "))
            except ValueError:
                print("Ungültige Eingabe. Bitte eine Zahl eingeben.")
                continue

            if g_input == solution:
                print("Richtig!")
                break
            else:
                if attempt < 2:
                    print("Falsch. Versuche es erneut.")
                else:
                    print(f"Falsch.\nDie richtige Antwort ist {solution}.")

if __name__ == "__main__":
    main()
