#This calculator was built in 2026
def calculator():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    operation = input("1: Addition (+)\n2: Subtraction (-)\n3: Multiplication (*)\n4: Division (/)\n"
                       "Please enter (1, 2, 3, 4): ")
    if operation == '1':
        sum = int(num1) + int(num2)
        print(f"The sum is: {sum}.")
    elif operation == '2':
        difference = int(num1) - int(num2)
        print(f"The difference is: {difference}.")
    elif operation == '3':
        product = int(num1) * int(num2)
        print(f"The product is: {product}.")
    elif operation == '4':
        if int(num2) == 0:
            print("You can't divide by 0!")
            return 0
        else:
            quotient = int(num1) / int(num2)
            print(f"The quotient is: {quotient}.")
    else:
        print("Unknown operation!")

calculator()