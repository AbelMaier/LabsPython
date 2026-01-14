def filter_lines(fisier_intrare, fisier_iesire, cuvant_cheie):

    f_in = open(fisier_intrare, "r", encoding="utf-8")
    lista_linii = f_in.readlines()
    f_in.close()

    f_out = open(fisier_iesire, "w", encoding="utf-8")

    for linie in lista_linii:
        # verific daca cuvantul cheie se afla in linie
        if cuvant_cheie in linie:

            f_out.write(linie)

    f_out.close()


print("Filtram liniile care contin 'Python'")

filter_lines("input1.txt", "filtered.txt", "Python")

print("Verifica fisierul 'filtered.txt'.")