class Caculator:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def addition(self):
        print("The Addition Of ", self.var1,"and",self.var2, "is", self.var1 + self.var2)
    def subtraction(self):
        print("The Subtraction Of ", self.var1, "and", self.var2, "is", self.var1 - self.var2)
    def multiplication(self):
        print("The Multiplication Of ", self.var1, "and", self.var2, "is", self.var1 * self.var2)
    def division(self):
        print("The Division Of ", self.var1, "and", self.var2, "is", self.var1/self.var2)


var2 = int(input("Enter The First Num:"))
var4 = int(input("Enter The Second Num:"))
operator = input("Enter The Operator:")

cal = Caculator(var2,var4)





if operator == "+":
    cal.addition()

elif operator == "-":
    cal.subtraction()

elif operator == "*":
    cal.multiplication()

elif operator == "/":
    cal.division()