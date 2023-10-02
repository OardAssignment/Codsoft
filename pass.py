import random
import string

def generate_password(length, complexity):
    if complexity < 1 or complexity > 4:
        print("Complexity level should be between 1 and 4.")
        return None

    characters = {
        1: string.ascii_letters,
        2: string.ascii_letters + string.digits,
        3: string.ascii_letters + string.digits + string.punctuation,
        4: string.ascii_letters + string.digits + string.punctuation + ' '
    }

    if length < 1:
        print("Password length should be at least 1.")
        return None

    password = ''.join(random.choice(characters[complexity]) for _ in range(length))
    return password

def main():
    print("********Password Generator**********")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            complexity = int(input("Enter the complexity level (1-4): "))

            password = generate_password(length, complexity)

            if password:
                print("Generated Password: " + password)
            
            break

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()


