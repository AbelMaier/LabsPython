text_introdus = input("Introdu valorile separate prin virgula: ")

# convertire in lista
lista_temporara = text_introdus.split(',')

# curatare spatii
lista_curata = []
for element in lista_temporara:
    # elimin spatiile de la inceput si final
    lista_curata.append(element.strip())

# creare tupla
tupla_mea = tuple(lista_curata)

print(f"Tupla creata este: {tupla_mea}")

# cerem valoarea de cautat
valoare_cautata = input("Care e valoarea cautata?: ")

# verificare si afisare
if valoare_cautata in tupla_mea:
    # pozitia primului element gasit
    pozitie = tupla_mea.index(valoare_cautata)
    print(f" Valoarea '{valoare_cautata}' se gaseste la indexul {pozitie}.")
else:
    print(f"Valoarea '{valoare_cautata}' nu exista in tupla.")