class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise ValueError("Salariul nu poate fi negativ!")

        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Angajat: {self.name}, Salariu: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        return f"Manager: {self.name}, Salariu: {self.salary}, Departament: {self.department}"


try:
    # creare angajat
    print("--- Introducere Angajat ---")
    emp_name = input("Nume Angajat: ")
    emp_salary = float(input("Salariu: "))

    emp = Employee(emp_name, emp_salary)

    # creare manager
    print("\n--- Introducere Manager ---")
    mgr_name = input("Nume Manager: ")
    mgr_salary = float(input("Salariu: "))
    mgr_department = input("Departament: ")

    mgr = Manager(mgr_name, mgr_salary, mgr_department)

    # afisare
    print("\nRezultate Salvate")
    print(emp.get_details())
    print(mgr.get_details())

except ValueError as e:
    print("Eroare:", e)