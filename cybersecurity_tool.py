import re

print("Cybersecurity Awareness Tool")

password = input("Enter a password: ")

if len(password) < 8:
    print("Weak Password - Use at least 8 characters")
elif re.search("[A-Z]", password) and re.search("[0-9]", password):
    print("Strong Password")
else:
    print("Moderate Password - Add numbers and uppercase letters")

url = input("Enter a website URL to check: ")

suspicious_words = ["login", "verify", "update", "secure"]

for word in suspicious_words:
    if word in url.lower():
        print("Warning: Suspicious URL detected")
        break
else:
    print("URL appears safe")
