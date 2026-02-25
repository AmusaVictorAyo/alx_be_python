# Defining a function that performs arithmetic operations based on the given operation type

def perform_operation(num1, num2, operation):
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        # Handling Zero division error for division operands
        case 'divide':
            if num2 == 0:
                return "Cannot divide by zero"
            elif num2 != 0:
                return num1 / num2
        case _:
            return "Invalid input"
