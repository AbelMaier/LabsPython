def imparte_numere(numar1, numar2):
    try:
        return numar1 / numar2
    except ZeroDivisionError:
        return None

try:
    a = float(input("Introdu primul numar: "))
    b = float(input("Introdu al doilea numar: "))

    # apelare functie
    rezultat = imparte_numere(a, b)

    if rezultat is None:
        print("Nu poti imparti la zero!")
    else:
        print(f"Rezultatul este: {rezultat}")
# verificare daca am introdus numere
except ValueError:
    print("Te rog introdu doar cifre!")
