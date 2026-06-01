import string
import secrets

def generate_password(length=12):
    choice = string.ascii_letters + string.digits 
    password = ''.join(secrets.choice(choice) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Generated password:", generate_password())

    