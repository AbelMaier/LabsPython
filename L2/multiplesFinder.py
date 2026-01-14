text_x = input("Introdu numărul x (baza): ")
text_y = input("Introdu numărul y (limita): ")

# verificare ambele numere sunt compuse din cifre

if text_x.isdigit() and text_y.isdigit():

    # convertire in int
    x = int(text_x)
    y = int(text_y)
    #inversarea valorilor in cazul in care x>y
    if x > y:
        x, y= y, x

    if x == 0:
        print("Eroare: 0 nu e un numar valid, nu are multiplii")

    else:
        print(f"Multiplii lui {x} mai mici decat {y} sunt:")
        # merg din x in x in loc sa merg din 1 in 1
        for numar in range(x, y, x):
            print(numar)

else:
    print("Eroare: Te rog introdu doar numere naturale pozitive.")