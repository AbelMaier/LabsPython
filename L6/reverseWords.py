def reverse_words(sentence):

    lista_cuvinte = sentence.split()

    # inversez lista
    lista_cuvinte.reverse()

    # noua propozitie
    text_nou = ""

    for cuvant in lista_cuvinte:
        if text_nou == "":
            text_nou = cuvant
        else:
            text_nou = text_nou + " " + cuvant

    return text_nou


print("Introdu propozitia:")
input_text = input()

if input_text == "":
    print("Nu ai introdus nimic.")
else:
    rezultat = reverse_words(input_text)

    print("Propozitia inversata:")
    print(rezultat)