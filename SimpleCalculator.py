A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))

operator = input("Enter an operator (+, -, *, /): ") 

if operator == "+":
    result = A + B
    print("The result is:", result)
elif operator == "-":
    result = A - B
    print("The result is:", result)
elif operator == "*":
    result = A * B
    print("The result is:", result)
elif operator == "/":
    if B != 0:
        result = A / B
        print("The result is:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator. Please use +, -, *, or /.")