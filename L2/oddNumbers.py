text_n = input("Introdu numarul n: ")

# verificare ca numarul sa fie numar valid
if text_n.isdigit():
    n = int(text_n)

    # verificare ca numarul sa fie pozitiv
    if n <= 0:
        print("Eroare: Te rog introdu un numar mai mare decat 0.")
    else:
        print(f"Numerele impare pana la {n} sunt:")
        for i in range(1, n + 1, 2):
            print(i)

else:
    print("Eroare: Te rog introdu un numar natural valid (fara litere).")