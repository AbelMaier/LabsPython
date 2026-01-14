def count_words_in_file(nume_fisier):
    # deschidere fisier
    f = open(nume_fisier, "r")

    # citire continut fisier
    continut = f.read()

    # inchidere fisier
    f.close()

    lista_cuvinte = continut.split()
    rezultat = len(lista_cuvinte)

    return rezultat


numar_cuvinte = count_words_in_file("example.txt")

print("Numarul total de cuvinte este:")
print(numar_cuvinte)