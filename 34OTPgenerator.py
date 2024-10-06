import random

def generate_otp():
    otp = random.randint(100000, 999999)
    return otp

# Example usage
otp = generate_otp()
print(f"Your OTP is: {otp}")