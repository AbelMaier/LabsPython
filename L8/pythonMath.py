import math

try:
    # citire
    input_num = input("Introdu un numar intreg pozitiv (ex: 25): ")
    num = int(input_num)

    if num < 0:
        print("Eroare: Te rog introdu un numar pozitiv!")
    else:
        input_angle = input("Introdu unghiul in grade (ex: 30): ")
        angle = float(input_angle)

        # radacina
        radacina = math.sqrt(num)

        # factorialul
        fact = math.factorial(num)

        # conversie in radiani
        unghi_in_radiani = math.radians(angle)
        # calcul sinus
        sinus = math.sin(unghi_in_radiani)

        # afisare
        print("\nRezultate:")
        print("Radacina patrata a " + str(num) + " este " + str(radacina))
        print("Factorialul lui " + str(num) + " este " + str(fact))
        print("Sinusul unghiului de " + str(angle) + " grade este " + str(round(sinus, 1)))

except ValueError:
    print("Nu ai introdus un format valid! (Numarul trebuie sa fie intreg, unghiul poate fi zecimal).")
