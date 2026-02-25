# Guard against negative input

while True:
    pattern = int(input("Enter the size of the pattern: "))

    if pattern < 0:
        continue
    else:
        break

size = 0

# Printing a square pattern of asterisks of the given size

while  size < pattern:

    for row in range(pattern):
        print("*", end="")
    print()
    size += 1