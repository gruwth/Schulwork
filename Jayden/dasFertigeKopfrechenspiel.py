import random

def main():
    operations = ['+', '-', '*', '/']
    score = 0

    num_of_tasks = int(input("Wie viele Aufgaben sollen es sein? "))
    num_of_tasks = min(num_of_tasks, 10)  # Max 10 Aufgaben

    for _ in range(num_of_tasks):
        operation = random.choice(operations)
        # operation = operations[random.randint(0, 3)]

        if operation == '+':
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 100)
        elif operation == '-':
            num1 = random.randint(1, 100)
            num2 = random.randint(1, num1)
        elif operation == '*':
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
        else:
            num2 = random.randint(1, 100)
            num1 = num2 * random.randint(1, 100)

        result = eval(f"{num1} {operation} {num2}")
        # print(result)

        print(f"Rechne im Kopf: {num1} {operation} {num2} = ?")

        while True:
            try:
                for attempt in range(3):
                    user_answer = int(input("Antwort: "))

                    if user_answer == result:
                        print(f"Glückwunsch du hast es in {attempt+1} geschaft.\n")
                        score += 1
                        break
                    else:
                        remaining_attempts = 2 - attempt
                        if remaining_attempts > 0:
                            print(f"Flasche antwort. Du hast {remaining_attempts} Versuche übrig.")
                        else:
                            print(f"Flasch, es ist {result}.")
                            break
                break
            except ValueError:
                print("Das war keine Zahl. Erneut eingeben.\n")
                print(f"Rechne im Kopf: {num1} {operation} {num2} = ?")
            

    print(f"Du hast {score} aus {num_of_tasks} Aufgaben richtig.")

if __name__ == "__main__":
    main()
