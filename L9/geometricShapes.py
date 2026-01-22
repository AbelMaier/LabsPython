import math

class Forma:
    def arie(self):
        pass

class Cerc(Forma):
    def __init__(self, raza):
        self.raza = raza

    def arie(self):
        try:
            return math.pi * (self.raza ** 2)
        except TypeError:
            return "ERROR: raza trebuie sa fie un numar!"

    def __str__(self):
        rezultat = self.arie()
        if isinstance(rezultat, (int, float)):
            return f"Cerc cu raza {self.raza} are aria {round(rezultat, 2)}"
        return f"Cerc - {rezultat}"

class Dreptunghi(Forma):
    def __init__(self, latime, inaltime):
        self.latime = latime
        self.inaltime = inaltime

    def arie(self):
        try:
            return self.latime * self.inaltime
        except TypeError:
            return "ERROR: latimea si inaltimea trebuie sa fie numere!"

    def __str__(self):
        rezultat = self.arie()
        if isinstance(rezultat, (int, float)):
            return f"Dreptunghi cu latime {self.latime} si inaltime {self.inaltime} are aria {rezultat}"
        return f"Dreptunghi - {rezultat}"


try:
    forme = [Cerc(5), Dreptunghi(10, 4)]

    for forma in forme:
        print(forma)

except Exception as e:
    print("ERROR:", e)
