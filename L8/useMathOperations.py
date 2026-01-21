import mathOperations

print("--- Testare Modul Propriu ---")

# definire numere pentru test
a = 10
b = 5

# apelari
rezultat_adunare = mathOperations.adunare(a, b)
print(f"Adunarea ({a} + {b}): {rezultat_adunare}")

rezultat_scadere = mathOperations.scadere(a, b)
print(f"Scaderea ({a} - {b}): {rezultat_scadere}")

rezultat_inmultire = mathOperations.inmultire(a, b)
print(f"Inmultirea ({a} * {b}): {rezultat_inmultire}")

rezultat_impartire = mathOperations.impartire(a, b)
print(f"Impartirea ({a} / {b}): {rezultat_impartire}")