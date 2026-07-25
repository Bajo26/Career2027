def get_username():
    while True:
        username = input("Enter your username: ").strip()
        
        if not username:
            print("Username cannot be empty.")
        else:
            break
    return username

def get_age():
    while True:
        try:
            get_age = int(input("Enter your age: "))
            if get_age <= 0:
                print("Age must be greater than zero.")
            else:
                break
        except ValueError:
            print("Invalid number!")
    return get_age

def display_info(username, age):
    print(f"Hello {username}!")
    print(f"You are {age} years old.")
    return username, age

def calculate_birth_year(age):
    current_year = 2026
    birth_year = current_year - age
    return birth_year
    
username = get_username()
age = get_age()

display_info(username, age)

birth_year = calculate_birth_year(age)
print(f"You were born in {birth_year}.")