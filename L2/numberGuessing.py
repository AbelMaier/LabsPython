import random

print(" JOC: GHICESTE NUMARUL (1-20) ")
print("Ai exact 5 incercari. Succes!")

# generare numar random
numar_secret = random.randint(1, 20)
#numarul de vieti
incercari_ramase = 5
#initializare numar ghicit
ghicire = -1

# jocul ruleaza cat timp utilizatorul mai are vieti ramase
while incercari_ramase > 0:

    print(f"\nVieti ramase: {incercari_ramase}")
    text_introdus = input("Introdu un numar intre 1 si 20: ")

    # verificare input
    if not text_introdus.isdigit():
        print("Eroare: Nu ai introdus un numar valid.")
        # bucla se reia, fara sa scada viata
        continue

    # conversie (doar daca a trecut de validare)
    ghicire = int(text_introdus)

    # verificarea numar valid in interval
    if ghicire < 1 or ghicire > 20:
        print("Eroare: Nu ai introdus un numar valid din range-ul [1,20]")
        # bucla se reia, fara sa scada viata
        continue

    # --- JOCUL PROPRIU ZIS ---

    if ghicire == numar_secret:
        print(f"BRAVO! Ai ghicit numarul {numar_secret}!")
        break  # bucla se inchide (castigator)

    elif ghicire < numar_secret:
        print("Prea mic!")
        incercari_ramase = incercari_ramase - 1  # scadem o viata

    else:  # e mai mare
        print("Prea mare!")
        incercari_ramase = incercari_ramase - 1  # scadem o viata


# verificam finalul jocului
if ghicire != numar_secret:
    print("\n--- GAME OVER ---")
    print(f"Nu mai ai vieti. Numarul secret era: {numar_secret}")