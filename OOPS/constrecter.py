# class Million_Coders:  # class
#
#     batch = "Morning"  # attribute
#
#     def __init__(self, name):  # constructor
#         self.name = name
#
#     def findBatch(self):
#         print(self.name, "is in batch of Morning")
#
#
# ubaid = Million_Coders("Sajid")  # object
# waqas = Million_Coders("Waqas")  # _
#
#
# ubaid.findBatch()
# waqas.findBatch()
#
# # print("Ubaid is batch of", ubaid.batch)  # calling class attribute using its


# class Person(object):
#
#     def __init__(self, name, idnumber):
#         self.name = name
#         self.idnumber = idnumber
#
#     def details(self):
#         print("My name is ", self.name)
#         print("IdNumber: ", self.idnumber)
#
#
# # child class
# class Employee(Person):
#     def __init__(self, name, idnumber, salary, post):
#         self.salary = salary
#         self.post = post
#
#         # invoking the _init_ of the parent class
#         Person.__init__(self, name, idnumber)
#
#     def employeedetails(self):
#         print("My name is {}".format(self.name))
#         print("IdNumber: {}".format(self.idnumber))
#         print("Salary: {}".format(self.salary))
#         print("Post: {}".format(self.post))

# creation of an object variable or an instance
# a = Employee('Hozaifa', 886012, 20000000, "Softwere Enginear")
#
# # calling a function of the class Person using
# # its instance
# a.employeedetails()
