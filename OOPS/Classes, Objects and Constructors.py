# class Employee:
#     pass
#
#
# Ubaid = Employee()
# Iqbal = Employee()
#
# Ubaid.Name = "Ubaid-UR-Rheman"
# Ubaid.Salary = "50000"
# Ubaid.Teacher = "Python Main Teacher"
#
# Iqbal.Name = "Muhammad Iqbal"
# Iqbal.Salary = "100000"
# Iqbal.Teacher = "Python Secondary Teacher"
#
# print(Ubaid.Name,"\n", Ubaid.Salary, "\n", Ubaid.Teacher, "\n", Iqbal.Name, "\n", Iqbal.Salary, "\n",  Iqbal.Teacher)


class Employee:
    def __init__(self, name, salary, teacher):
        self.Name = name
        self.Salary = salary
        self.Teacher = teacher


Ubaid = Employee('Ubaid-Ur-Rheman', 50000, 'Python Main Teacher')
Iqbal = Employee('Muhammad Iqbal', 100000, 'Python Secondary Teacher')
print(Ubaid.Name,"\n", Ubaid.Salary, "\n", Ubaid.Teacher, "\n", Iqbal.Name, "\n", Iqbal.Salary, "\n",  Iqbal.Teacher)