while True:
        username = input("Enter your username: ").strip()
        
        if not username:
            print("Username cannot be empty.")
        else:
            break
    
while True:
    try:
        age = int(input("Enter your age: "))
        if age <= 0:
            print("Age must be greater than zero.")
        else:
            break
    except ValueError:
        print("Invalid number!")
              
print(f"Hello {username}!")
print(f"You are {age} years old.")

   