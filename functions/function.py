def sum(num, num2):
    return num + num2

#print(sum(1, 10))


def operations():
    print("1. addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (x)")
    print("4. Division (/)")
    print("5. Quit")

def sum(num, num1):
    return num + num1

def sub(num, num1):
    return num - num1

def multiply(num, num1):
    return num * num1

def divide(num, num1):
    if num1 > 0:
        return num / num1
    else:
        print("Error: Division by zero is not allowed")
        return 0

operations()

choice = int(input("Enter your choice: "))

if choice == 1:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Sum is: ", sum(num1, num2))

elif choice == 2:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Subtraction is: ", sub(num1, num2))

elif choice == 3:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The multiplication is: ", multiply(num1, num2))

elif choice == 4:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The division is: ", divide(num1, num2))

else:
    print("Invalid choice")