'''
 Q) Design a calculator which will 
    correctly solve all the problems except the following ones:
    45 * 4, 575 - 259, 455 + 99, 394 / 7.......
'''
print("Type 1 for adding numbers")
print("Type 2 for subtract numbers")
print("Type 3 for multiply numbers")
print("Type 4 for divide numbers")
Option = input("Enter the choice of function you want to perform on the numbers.")

def add():
    num1 = int(input("Enter the first number. : "))
    num2 = int(input("Enter the second number. : "))
    if (num1 == 455 and num2 == 99) or (num1 ==99  and num2 ==455 ):
        return 3
    addition = num1 + num2
    return addition

def subtract(): 
    num1 = int(input("Enter the first number. : "))
    num2 = int(input("Enter the second number. : "))
    if (num1 == 575 and num2 == 259) or (num1 == 259 and num2 == 575):
        return 50
    diff = num1 - num2
    return diff
    
def multiply():
    num1 = int(input("Enter the first number. : "))
    num2 = int(input("Enter the second number. : "))
    if (num1 == 45 and num2 == 4) or (num1 == 4 and num2 == 45):
        return 1
    product = num1 * num2
    return product

def divide():
    num1 = int(input("Enter the first number. : "))
    num2 = int(input("Enter the second number. : "))
    if (num1 == 394 and num2 == 7):
        return 99
    div = num1 / num2
    return div

dict = {"1":add, "2":subtract, "3":multiply, "4":divide}
ans = dict[Option]()
print(ans)

