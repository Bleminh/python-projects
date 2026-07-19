def calculator():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    operation = input("Choose (+, -, *, /): ")
    if operation == '+':
        sum = int(num1) + int(num2)
        print(f"The sum is: {sum}.")
    elif operation == '-':
        difference = int(num1) - int(num2)
        print(f"The difference is: {difference}.")
    elif operation == '*':
        product = int(num1) * int(num2)
        print(f"The product is: {product}.")
    elif operation == '/':
        if int(num2) == 0:
            print("You can't divide by 0!")
            return 0
        else:
            quotient = int(num1) / int(num2)
            print(f"The quotient is: {quotient}.")
    else:
        print("Unknown operation!")

calculator()