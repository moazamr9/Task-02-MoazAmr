print("Please enter the key: ", end="")
key = int(input())

print("Please enter the plaintext: ", end="")
plaintext = input()

ciphertext = ""

for char in plaintext:
    if char.isalpha():
        if char.isupper():
            ciphertext += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            ciphertext += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
    else:
        ciphertext += char

print("Ciphertext:", ciphertext)