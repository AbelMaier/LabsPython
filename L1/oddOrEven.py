try:
    x = int(input("Dati numarul: "))

    if x % 2 == 0:
        print("Numarul este par")
    else:
        print("Numarul este impar")

except ValueError:
    print("Nu ai introdus un numar intreg valid.")