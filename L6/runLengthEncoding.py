def run_length_encoding(text):
    if text == "":
        return ""

    caracter_curent = text[0]
    numaratoare = 1

    rezultat = ""

    # parcurg textul incepand de la a doua litera
    for i in range(1, len(text)):
        litera = text[i]

        # verific daca e aceeasi litera ca cea de dinainte
        if litera == caracter_curent:
            numaratoare = numaratoare + 1
        else:
            rezultat = rezultat + caracter_curent + str(numaratoare)

            # resetare contor pentru noua litera
            caracter_curent = litera
            numaratoare = 1


    rezultat = rezultat + caracter_curent + str(numaratoare)

    return rezultat


print("Introdu textul de comprimat (ex: aaabbb):")
input_text = input()

if input_text == "":
    print("Nu ai introdus nimic.")
else:
    rezultat_comprimat = run_length_encoding(input_text)
    print("Rezultat:")
    print(rezultat_comprimat)