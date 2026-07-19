user_name = input("Enter your username: ")
while True:
    try:
        age = int(input("Enter your age: "))
        if age <= 0:
            print("Age must be greater than zero.")
        else:
            break
    except ValueError:
        print("Invalid number!")

print(f"Hello {user_name}!")
print(f"You are {age} years old.")

