# Caesar Cipher Program
# This program can encrypt and decrypt a message using a shift value

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result


def decrypt(text, shift):
    # decrypting is the same as encrypting, just with a negative shift
    return encrypt(text, -shift)


# Main program starts here
print("Caesar Cipher Program")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter choice (1 or 2): ")
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

if choice == "1":
    result = encrypt(message, shift)
    print("Encrypted message:", result)
elif choice == "2":
    result = decrypt(message, shift)
    print("Decrypted message:", result)
else:
    print("Invalid choice")
