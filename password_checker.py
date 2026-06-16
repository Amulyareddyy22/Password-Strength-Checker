password = input("Enter a password: ")

common_passwords = [
    "password",
    "123456",
    "password123",
    "admin",
    "qwerty"
]

if password.lower() in common_passwords:
    print("WARNING: This is a commonly used password!")

score = 0

if len(password) >= 8:
    score += 1
else:
    print("Password should be at least 8 characters.")

if any(char.isupper() for char in password):
    score += 1
else:
    print("Add an uppercase letter.")

if any(char.islower() for char in password):
    score += 1
else:
    print("Add a lowercase letter.")

if any(char.isdigit() for char in password):
    score += 1
else:
    print("Add a number.")

special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

if any(char in special_chars for char in password):
    score += 1
else:
    print("Add a special character.")

print(f"\nScore: {score}/5")

if score <= 2:
    print("Password Strength: Weak")
elif score <= 4:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")
