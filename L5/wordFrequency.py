def word_frequency(text):
    # transform textul in litere mici
    text_mic = text.lower()

    # elimin punctuatia
    semne_punctuatie = ".,!?;:" #definire caractere speciale pentru a le scoate din text
    text_curat = ""

    # parcurg textul litera cu litera
    for caracter in text_mic:
        # daca caracterul nu e semn de punctuatie, il pastrez
        if caracter not in semne_punctuatie:
            text_curat = text_curat + caracter
        else:
            # daca e punctuatie, il inlocuiesc cu un spatiu
            text_curat = text_curat + " "

    #impart textul intr-o lista de cuvinte
    lista_cuvinte = text_curat.split()

    # dictionarul de frecventa
    dictionar = {}

    for cuvant in lista_cuvinte:
        # verific daca am mai intalnit cuvantul
        if cuvant in dictionar:
            # daca exista deja, +1 frectventa
            dictionar[cuvant] = dictionar[cuvant] + 1
        else:
            # daca nu exista, il adaug cu valoarea 1
            dictionar[cuvant] = 1

    return dictionar


print("Introduceti textul:")
text_utilizator = input()

if text_utilizator == "":
    print("Nu ati introdus niciun text.")
else:
    rezultat = word_frequency(text_utilizator)
    print("Frecventa cuvintelor este:")
    print(rezultat)