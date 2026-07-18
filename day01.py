
name = input("Enter your name: ")
try:
    age = int(input("Enter your age: "))
    next_age = age + 1
    total = age * 365
    print(f"Hello, {name}!")
    print(f"Next year, you'll be {next_age} years old.")
    print(f"The total number of days you've approximately lived {total} days.")
except ValueError:
    print("Error: That was not a valid number of age!")