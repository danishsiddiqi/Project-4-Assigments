import hashlib

def hash_password(password):

    return hashlib.sha256(password.encode()).hexdigest()
stored_logins ={
    'admin@example.com': hash_password('admin123'),
    'user@example.com': hash_password('user123')
}

def login(email, password):
    if email in stored_logins and stored_logins[email] == hash_password(password):
        return True
    else:
        return False
email = input("Enter your email: ")
password = input("Enter your password: ")


if login(email, password):
    print("Login successful!")
else:
    print("Invalid email or password.")


