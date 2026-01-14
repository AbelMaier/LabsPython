text_introdus = input("Introdu numerele separate prin virgula: ")

try:
    lista_text = text_introdus.split(',')

    # convertire in int
    lista_numere = []
    for element in lista_text:
        # scoatem spatiile
        lista_numere.append(int(element.strip()))

    lista_unica = []

    for numar in lista_numere:
        # verificare daca am adaugat numarul in lista finala
        if numar not in lista_unica:
            # daca nu e acolo, il adaugam, daca e deja, il ignoram
            lista_unica.append(numar)

    # afisare
    print(f"Lista originala: {lista_numere}")
    print(f"Lista fara duplicate (ordonata): {lista_unica}")

except ValueError:
    print("Eroare: Te rog introdu doar numere intregi, separate prin virgula.")