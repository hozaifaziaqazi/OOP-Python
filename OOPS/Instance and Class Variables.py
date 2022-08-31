class Employee:
    Bonus = 1.5

    def __init__(self, name, salary, teacher):
        self.Name = name
        self.Salary = salary
        self.Teacher = teacher
        self.Bonus = 1.5

    def increase(self):
        self.Salary = int(self.Salary * self.Bonus)


Ubaid = Employee('Ubaid-Ur-Rheman', 50000, 'Python Main Teacher')
Iqbal = Employee('Muhammad Iqbal', 100000, 'Python Secondary Teacher')
print(Iqbal.Salary)
Iqbal.increase = 9
Iqbal.increase()
print(Iqbal.Salary)
print(Ubaid.__dict__, '\n')
print(Iqbal.__dict__)
# print(Ubaid.Name,"\n", Ubaid.Salary, "\n", Ubaid.Teacher, "\n", Iqbal.Name, "\n",
# Iqbal.Salary, "\n",  Iqbal.Teacher)
