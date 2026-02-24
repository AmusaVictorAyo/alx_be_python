number = int(input("Enter a number to see its multiplication table: "))

X = number

for numbers in range(1, 11):
    Y = numbers
    Z = X * Y
    print(f"{X} * {Y} = {Z}")