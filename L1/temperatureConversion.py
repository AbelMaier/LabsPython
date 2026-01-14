text_input = input("Introdu temperatura în grade Celsius: ")

text_input_corectat = text_input.replace(',', '.')

try:
    # Încercăm conversia
    celsius = float(text_input_corectat)

    # Dacă conversia reușește, facem calculul
    fahrenheit = celsius * 9 / 5 + 32
    print(f"Temperatura în Fahrenheit este: {fahrenheit}")

except ValueError:
    # Dacă apare o eroare la conversie (ex: litere), intrăm aici
    print("valoare invalida, trebuie sa fie numar")