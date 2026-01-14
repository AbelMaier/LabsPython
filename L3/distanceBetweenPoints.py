import math

# functia care calculeaza distanta
def distance(x1, y1, x2, y2):
    #ridicare la putere
    x = (x2 - x1) ** 2
    y = (y2 - y1) ** 2

    return math.sqrt(x + y)


while True:
    try:
        # citesc toate cele 4 coordonate
        x1 = float(input("Introdu x1: "))
        y1 = float(input("Introdu y1: "))
        x2 = float(input("Introdu x2: "))
        y2 = float(input("Introdu y2: "))

        # calculam distanta
        # apelare functie
        dist = distance(x1, y1, x2, y2)

        # afisam rezultatul, 2 zecimale
        print(f"Distanta dintre puncte este: {dist:.2f}")

        # dupa calcul, bucla se opreste
        break

    except ValueError:
        print("Eroare: Te rog introdu doar numere reale (ex: 5, -2, 3.5).")
        print("Sa incercam din nou...\n")