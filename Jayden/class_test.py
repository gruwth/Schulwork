class Artikel:


    def __init__(self, name:str, preis:int, bestand:int):
        self.name = name
        self.preis = preis
        self.bestand = bestand
    


    def kaufen (self, menge):
        if self.bestand >= menge:
            self.bestand -= menge
            return True

    def auffuellen (self, menge):
        self.bestand += menge

    def preis_anpassen (self, neuer_preis):
        self.preis = neuer_preis
    
    def umbenennen (self, neuer_name):
        self.name = neuer_name

    def anzeigen (self):
        print(f"Name: {self.name}, Preis: {self.preis}, Bestand: {self.bestand}")


banana = Artikel("Banane",2.5,500)

# while True:
#     Aufgabe=int(input("was wollen sie tuen\n1. Kaufen\n2. Auffüllen\n3. Preis anpassen\n4. Artikel umbenennen\n5. Anzeigen"))
