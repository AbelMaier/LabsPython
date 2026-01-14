def factorial(n):
    # cazul special: 0! este 1
    if n == 0:
        return 1

    produs = 1

    # parcurg de la 1 pana la n
    for i in range(1, n + 1):
        produs = produs * i

    return produs

text_n = input("Introdu un numar intreg: ")

# validare date intrare
if text_n.isdigit():
    n = int(text_n)

    # apelare functie
    rezultat = factorial(n)

    print(f"Factorialul lui {n} este: {rezultat}")

else:
    print("Eroare: Trebuie sa introduci un numar natural (fara litere, fara minus, fara virgula).")