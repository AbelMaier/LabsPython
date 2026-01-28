class Inventar:
    def __init__(self):
        self.produse = {
            "mere": 50,
            "pere": 30,
            "apa": 100,
            "paine": 20
        }

    def seteaza_stoc(self, nume, cantitate):
        if cantitate < 0:
            raise ValueError("Cantitatea nu poate fi negativa!")
        self.produse[nume] = cantitate

    def cauta(self, nume):
        return self.produse[nume]


magazin = Inventar()

try:
    print(f"Produse existente deja in stoc: {list(magazin.produse.keys())}")

    print("--- Pasul 1: Adaugam un produs NOU (sau actualizam) ---")
    prod = input("Nume produs: ")
    cant = int(input("Cantitate: "))

    # Adaugam produsul introdus de tine
    magazin.seteaza_stoc(prod, cant)
    print("Produs salvat/actualizat!")

    print("\n--- Pasul 2: Cautam un produs ---")
    # Acum poti cauta fie ce ai adaugat tu, fie "mere", "apa" etc.
    cautat = input("Ce produs cauti? (incearca 'mere' sau ce ai adaugat tu): ")

    stoc_gasit = magazin.cauta(cautat)
    print(f"Produsul '{cautat}' are stocul: {stoc_gasit}")

except ValueError:
    print("Eroare: Ai introdus litere sau un numar negativ!")
except KeyError:
    print("Eroare: Produsul cautat nu exista in inventar!")