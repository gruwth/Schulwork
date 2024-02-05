import random
temperatur = round(random.uniform(-15.0,5.0), 1)
eingabe = str(input())
match eingabe:
    case "R" | "r":
        print("Radio wurde aktiviert")
    case "N" | "n":
        print("Navigation aktiviert")
    case "T" | "t":
        print("Temperaturanzeige aktiviert")
        tempÜN = [i / 10 for i in range(1, 10001)]
        tempUN = [-x for x in tempÜN]
        match temperatur in tempUN:
            case True:
                print(f"Die Außentemperatur beträgt {temperatur}°C \nAchtung, Glättegefahr!")
        match temperatur in tempÜN:
            case True:
                print(f"Die Außentemperatur beträgt {temperatur}°C")
        match temperatur:
            case 0:
                print(f"Die Außentemperatur beträgt {temperatur}°C \nGefrierpunkt erreicht!")
    case _:
        print("Falsche Eingabe!")