def inverted_index(documents):
    # dictionarul in care vom stoca rezultatele
    index_dict = {}

    # nr de documente
    nr_documente = len(documents)

    for i in range(nr_documente):

        text = documents[i]

        lista_cuvinte = text.split()

        for cuvant in lista_cuvinte:
            # verific daca cuvantul este deja in dictionar
            if cuvant not in index_dict:
                # daca nu e, creez o intrare noua cu un set gol
                index_dict[cuvant] = set()

            # adaugam indexul documentului curent in setul cuvantului
            index_dict[cuvant].add(i)

    return index_dict


print("Cate propozitii vrei sa introduci?")
input_numar = input()

if input_numar == "":
    print("Nu ai introdus un numar.")
else:
    numar = int(input_numar)

    # creez o lista goala unde voi pune propozitiile
    lista_documente = []

    print("Introdu propozitiile pe rand:")

    for k in range(numar):
        print("Documentul " + str(k) + ":")
        propozitie = input()
        lista_documente.append(propozitie)

    #apelare functie
    rezultat = inverted_index(lista_documente)

    print("\n--- Afisare detaliata ---")
    for cuvant in rezultat:
        print(cuvant + ": " + str(rezultat[cuvant]))