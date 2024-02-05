def stellenwert_umrechner(eingabe_text, basis):
    summe = 0
    print("Umgewandelt wird", eingabe_text)
          
    anzahl_der_stellen = len(eingabe_text)
    print("Anzahl der Stellen", anzahl_der_stellen)
          
    exponent = 0
    for aktuelle_stelle in range(anzahl_der_stellen, 0, -1):
        print("Stelle Nr.", aktuelle_stelle, "Wert", eingabe_text[aktuelle_stelle-1], "mit der Stellenwertigkeit", str(pow(basis, exponent)))
        summe = summe + int(eingabe_text[aktuelle_stelle-1]) * pow(basis, exponent)
        exponent = exponent + 1
    return summe

def zahl_umrechner(dezimalzahl, basis):
    ausgabe_text = ""
    
    power_of_basis = pow(basis, 0)
    while dezimalzahl > 0:
        stellenwert = dezimalzahl % basis
        dezimalzahl = dezimalzahl // basis
        ausgabe_text = str(stellenwert) + ausgabe_text
    return ausgabe_text

print(stellenwert_umrechner("123", 7))  
print(zahl_umrechner(66, 7))
