def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
def exp(a, b):
    return a ** b
def sqre(a):
    return a ** 2
def sqrtt(a):
    return a ** 0.5
print("Calculator")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exponent")
print("6.Square")
print("7.Square Root")
choice = int(input("Enter your choice: "))
if choice in [1, 2, 3, 4, 5]:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    if choice == 1:
        print(add(x, y))
    elif choice == 2:
        print(sub(x, y))
    elif choice == 3:
        print(mul(x, y))
    elif choice == 4:
        print(div(x, y))
    elif choice == 5:
        print(exp(x, y))
elif choice == 6:
    x = float(input("Enter number: "))
    print(sqre(x))
elif choice == 7:
    x = float(input("Enter number: "))
    print(sqrtt(x))
else:
    print("Invalid choice")
