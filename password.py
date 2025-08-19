import random
import string

def create_pass(length=8):
     characters = string.ascii_letters + string.digits + string.punctuation
     password = ''.join(random.choice(characters) for _ in range(length))
     return password


print("🔑 Welcome to Password Generator")

length = int(input("Enter password length: "))
new_password = create_pass(length)
print("✅ Your new password is:", new_password)