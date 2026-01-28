def calculeaza_suma_din_fisier(nume_fisier):
    suma_totala = 0

    try:
        with open(nume_fisier, "r", encoding="utf-8") as f:


            for i, linie in enumerate(f, 1):
                linie = linie.strip()
                try:
                    numar = float(linie)
                    suma_totala += numar

                except ValueError:
                    # afisare rand nevalid
                    print(f"[Randul {i}] : Linia nu este valida.")

        return suma_totala

    except FileNotFoundError:
        print(f"Eroare: Fisierul '{nume_fisier}' nu a fost gasit!")
        return None
    except Exception as e:
        print(f"A aparut o alta eroare la citire: {e}")
        return None

nume = input("Introdu numele fisierului (ex: numere.txt): ")

rezultat = calculeaza_suma_din_fisier(nume)

if rezultat is not None:

    print(f"\nSuma totala a numerelor valide este: {rezultat}")