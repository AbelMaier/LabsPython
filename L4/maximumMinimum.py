text_introdus = input("Introdu numerele separate prin virgula: ")

try:
    lista_text = text_introdus.split(',')

    # cream o lista goala unde vom pune numerele
    lista_numere = []

    # conversie
    for element in lista_text:
        numar = int(element)

        # Adaugam numarul in lista noastra finala
        lista_numere.append(numar)

    #afisare minim si maxim

    if len(lista_numere) > 0:
        print(f"Lista ta este: {lista_numere}")
        print(f"Maximul este: {max(lista_numere)}")
        print(f"Minimul este: {min(lista_numere)}")
    else:
        print("Lista este goala.")

except ValueError:
    print("Eroare: Asigura-te ca ai introdus doar numere separate prin virgula.")