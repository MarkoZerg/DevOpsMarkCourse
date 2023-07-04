# It's a calculator on python

# Function multiplication


def multiplication(a, b):
    result = float(a) * float(b)
    return str(result)

# Function division


def division(a, b):
    result = float(a) / float(b) if b > 0 else "division by zero is not allowed"
    return str(result)

# Function addition


def addition(a, b):
    result = float(a) + float(b)
    return str(result)

# Function subtraction


def subtraction(a, b):
    result = float(a) - float(b)
    return str(result)

# Starting message


print("Welcome to the Calculator Program")

while True:
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting the calculator program...")
        break

    (a) = float(input("Enter the first number: "))
    (b) = float(input("Enter the second number: "))

    if choice == '1':
        print("Result: " + addition(a, b))
    elif choice == '2':
        print("Result: " + subtraction(a, b))
    elif choice == '3':
        print("Result: " + multiplication(a, b))
    elif choice == '4':
        print("Result: " + division(a, b))
    else:
        print("Invalid input. Please enter a valid choice.")
