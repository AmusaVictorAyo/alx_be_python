# Collect the first and second number.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Choosing preferred operation
operation = input("Choose the operation (+, -, *, /): ")


match operation:

    case '+':
        result = num1 + num2
        print(f"The result is {result}")
    case '-':
        result = num1 - num2
        print(f"The result is {result}")
    case '*':
        result = num1 * num2
        print(f"The result is {result}")
    
    # Handling Dividion by Zero
    case '/':
        if num1 == 0 or num2 ==0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}")