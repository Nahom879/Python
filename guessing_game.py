import random

input("Welcome to my number guessing game.")
num = random.randint(1, 10)
guess = int(input("Enter a number(1-10): "))

a = 0
while a == 0:
    def compare(a, b):
        if a == b:
            return "Congratulation. You got the number correct."
        elif a < b:
            return "Your number is too low."
        elif a > b:
            return "Your number is too high"
        return None
    print(compare(guess, num))
    break