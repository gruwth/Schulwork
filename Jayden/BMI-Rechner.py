gewicht = float(input("Geben Sie Ihr Gewicht in Kilogramm ein: "))
groesse = float(input("Geben Sie Ihre Größe in Metern ein: "))
alter = int(input("Geben Sie Ihr Alter ein: "))

if alter < 18:
    print("Sie sind noch minderjährig.")
else:
    print("Sie sind erwachsen.")

    bmi = gewicht / (groesse * groesse)

    if bmi < 18.5:
        kategorie = "Untergewicht"
    elif bmi < 24.9:
        kategorie = "Normalgewicht"
    elif bmi < 29.9:
        kategorie = "Übergewicht"
    else:
        kategorie = "Adipositas"

    print(f"Ihr BMI beträgt: {bmi:.2f}")
    print(f"Sie befinden sich in der Kategorie: {kategorie}")


