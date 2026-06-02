import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4"

    characters = string.ascii_letters + string.digits + string.punctuation

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    password += random.choices(characters, k=length - 4)
    random.shuffle(password)

    return ''.join(password)

def main():
    print("Random Password Generator")

    try:
        length = int(input("Enter password length: "))
        password = generate_password(length)
        print("Generated Password:", password)
    except:
        print("Invalid input")

if __name__ == "__main__":
    main()