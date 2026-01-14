def reverse_lines(fisier_intrare, fisier_iesire):
    # Adaugam encoding="utf-8" pentru a suporta diacriticele
    f_in = open(fisier_intrare, "r", encoding="utf-8")

    # citim pe randuri
    lista_linii = f_in.readlines()

    f_in.close()

    f_out = open(fisier_iesire, "w", encoding="utf-8")

    for linie in lista_linii:
        # scap de \n de la final
        linie_curata = linie.strip()

        # inversare linie
        linie_inversa = linie_curata[::-1]

        # scriere in noul fisier
        f_out.write(linie_inversa + "\n")

    f_out.close()


reverse_lines("input.txt", "output.txt")

print("Textul a fost inversat si scris in fisierul 'output.txt'")
