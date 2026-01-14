text_introdus = input("Introdu scorul procentual (0-100): ")

if text_introdus.isdigit():

    scor = int(text_introdus)

    if scor > 100:
        print("Eroare: Scorul nu este valid. Te rog introdu o valoare din intervalul [0,100]")
    else:
        if scor >= 90:
            print("Nota A")
        elif scor >= 80:
            print("Nota B")
        elif scor >= 70:
            print("Nota C")
        elif scor >= 60:
            print("Nota D")
        else:
            print("Nota F")

else:
    print("Valoarea introdusa este invalida, introdu un numar din intervalul [0,100]")