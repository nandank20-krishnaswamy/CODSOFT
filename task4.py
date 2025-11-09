# Password Generator
# Expanded student project

import random
import string

def generate_password(length, complexity):
    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator")
    print("This program will help you create strong random passwords.")
    
    while True:
        try:
            length = int(input("\nEnter the desired password length: "))
            if length <= 0:
                print("Password length must be greater than zero.")
                continue

            print("\nChoose complexity level:")
            print("1. Letters only")
            print("2. Letters and digits")
            print("3. Strong (letters, digits, symbols)")
            
            try:
                complexity = int(input("Enter choice (1/2/3): "))
                if complexity not in [1, 2, 3]:
                    print("Invalid choice. Please select 1, 2, or 3.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            count = input("\nHow many passwords do you want to generate? (default 1): ")
            try:
                count = int(count) if count else 1
            except ValueError:
                print("Invalid input. Generating 1 password by default.")
                count = 1

            print("\nGenerated Passwords:")
            for i in range(count):
                password = generate_password(length, complexity)
                print(f"{i+1}. {password}")

            again = input("\nDo you want to generate more passwords? (yes/no): ").lower()
            if again != "yes":
                print("Goodbye!")
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
