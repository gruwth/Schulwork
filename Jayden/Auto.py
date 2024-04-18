# Definition der Klasse "Auto"
class Auto:
    def __init__(self, marke: str, farbe: str, baujahr: int):
        try:
            if not isinstance(marke, str):
                raise ValueError("marke must be a string")
            if not isinstance(farbe, str):
                raise ValueError("farbe must be a string")
            if not isinstance(baujahr, int):
                raise ValueError("baujahr must be an integer")
            self.marke = marke
            self.farbe = farbe
            self.baujahr = baujahr
        except ValueError as e:
            print(e)
            exit(1)
        

    def beschleunigen(self):
        print(f"{self.marke} beschleunigt!")

# Erstellen von Objekten basierend auf der Klasse "Auto"
volkswagen_beetle = Auto(1, "rot", 2015)
ford_mustang = Auto("Ford Mustang", "blau", 2020)

# Zugriff auf Eigenschaften und Methoden der Objekte
print(f"Das Auto ist ein {volkswagen_beetle.marke}, es ist {volkswagen_beetle.farbe} und wurde im Jahr {volkswagen_beetle.baujahr} hergestellt.")
volkswagen_beetle.beschleunigen()

print(f"Das Auto ist ein {ford_mustang.marke}, es ist {ford_mustang.farbe} und wurde im Jahr {ford_mustang.baujahr} hergestellt.")
ford_mustang.beschleunigen()
