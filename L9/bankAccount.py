class BankAccount:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance = self._balance + amount
        print(f"Ai depus {amount} lei.")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance = self._balance - amount
            print(f"Ai retras {amount} lei.")
        else:
            print("Eroare: Fonduri insuficiente!")

    def get_balance(self):
        return self._balance

contul_meu = BankAccount()

print(f"Sold curent: {contul_meu.get_balance()} lei")
suma_depunere = float(input("Introdu suma pe care vrei sa o depui: "))

# apelare metoda depunere suma
contul_meu.deposit(suma_depunere)

print(f"Sold curent: {contul_meu.get_balance()} lei")
suma_retragere = float(input("Introdu suma pe care vrei sa o retragi: "))

# apelare metoda retragere
contul_meu.withdraw(suma_retragere)

# afisare sold final
print(f"Sold final in cont: {contul_meu.get_balance()} lei")
