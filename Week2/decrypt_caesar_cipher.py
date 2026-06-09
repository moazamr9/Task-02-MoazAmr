print("Please enter a cipher text to encrypt: ", end="")
cipher = input()

print("Please enter the key: ", end="")
key = int(input())

plaintext = ""
for char in cipher:
    if char.isalpha():
        if char.isupper():
            plaintext += chr((ord(char) - ord('A') - key) % 26 + ord('A'))
        else:
            plaintext += chr((ord(char) - ord('a') - key) % 26 + ord('a'))
    else:
        plaintext += char

print("Plaintext:", plaintext)