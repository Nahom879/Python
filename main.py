input("Welcome to my calculator program.")
first_number = int(input("Enter the first number: "))
operation = input("Enter the operation(+, -, *, /): ")
second_number = int(input("Enter the second number: "))

def calculation(first_number, second_number, operation):
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        if second_number == 0:
            print("You cannot divide by zero!")
        else:
            return first_number / second_number
    else:
        print("Invalid input")

print(calculation(first_number, second_number, operation))