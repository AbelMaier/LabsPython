class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)

        self.department = department

    def get_details(self):
        return f"Manager: {self.name}, Salary: {self.salary}, Department: {self.department}"


print("\n Adauga un Manager nou ")
nume_mgr = input("Nume Manager: ")
salariu_mgr = int(input("Salariu: "))
dept_mgr = input("Departament: ")

manager_nou = Manager(nume_mgr, salariu_mgr, dept_mgr)

print("\nDetalii salvate:")
print(manager_nou.get_details())