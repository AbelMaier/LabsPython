def unique_pair_sum(numbers, target):
    # creez un set pentru a elimina duplicatele
    perechi = set()

    # lungimea listei
    n = len(numbers)

    # trec prin lista, luand un element si verificandu-l cu restul listei
    for i in range(n):
        for j in range(i + 1, n):

            numar1 = numbers[i]
            numar2 = numbers[j]

            # verific daca suma lor este cea cautata
            if numar1 + numar2 == target:
                if numar1 < numar2:
                    pereche = (numar1, numar2)
                else:
                    pereche = (numar2, numar1)

                # adaug perechea in set
                perechi.add(pereche)

    return perechi


print("Introdu numerele separate prin spatiu:")
text_input = input()

if text_input == "":
    print("Nu ai introdus numere.")
else:
    lista_siruri = text_input.split()

    # convertesc sirurile in numere intregi
    numbers_list = []
    for element in lista_siruri:
        numbers_list.append(int(element))

    print("Introdu valoarea tinta:")
    target_input = input()

    if target_input == "":
        print("Nu ai introdus tinta.")
    else:
        target_val = int(target_input)

        rezultat = unique_pair_sum(numbers_list, target_val)

        print("Perechile gasite sunt:")
        print(rezultat)