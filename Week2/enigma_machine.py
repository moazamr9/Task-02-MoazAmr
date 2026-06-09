# Read the text and make it to uppercase
text = input("Please enter the text to encrypt or decrypt: ")
text = text.upper()

# Dictionary to store the rotor wirings and positions
rotors = {
    1: {
        "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        "position": 0
    },
    2: {
        "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
        "position": 0
    },
    3: {
        "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
        "position": 0
    },
    4: {
        "wiring": "ESOVPZJAYQUIRHXLNFTGKDCMWB",
        "position": 0
    },
    5: {
        "wiring": "VZBRGITYUPSDNHLXAWMJQOFECK",
        "position": 0
    }
}

# Copy the selected rotors to another dictionary
selected_rotors = {}

# Function to check if the rotor choice is valid and not already selected
def check_rotor_choice(rotor):
    while rotor in range (1, 6) and (rotors[rotor]["wiring"] not in [i["wiring"] for i in selected_rotors.values()]):
        return rotor
    else:
        print("Invalid rotor choice. Please select a rotor between 1 and 5: ", end="")
        rotor = int(input())
        return check_rotor_choice(rotor)

# Function to check if the initial position is valid
def check_initial_position(position):
    while position in range (1, 27):
        return position
    else:
        print("Invalid initial position. Please enter a number between 1 and 26: ", end="")
        position = int(input())
        return check_initial_position(position)

# Get the rotor choices and initial positions from the user
print("Please select the first rotor (right to left) you will use (1-5): ", end="")
selected_rotors[1] = rotors[check_rotor_choice(int(input()))].copy()
print("Please select the second rotor (right to left) you will use (1-5): ", end="")
selected_rotors[2] = rotors[check_rotor_choice(int(input()))].copy()
print("Please select the third rotor (right to left) you will use (1-5): ", end="")
selected_rotors[3] = rotors[check_rotor_choice(int(input()))].copy()
print("Please enter the initial position of the first rotor (right to left) (1-26): ", end="")
rotor1_position = check_initial_position(int(input()))
print("Please enter the initial position of the second rotor (right to left) (1-26): ", end="")
rotor2_position = check_initial_position(int(input()))
print("Please enter the initial position of the third rotor (right to left) (1-26): ", end="")
rotor3_position = check_initial_position(int(input()))

# Set the initial positions of the selected rotors
selected_rotors[1]["position"] = rotor1_position - 1
selected_rotors[2]["position"] = rotor2_position - 1
selected_rotors[3]["position"] = rotor3_position - 1

# Function to step the rotors
def rotor_step():
    selected_rotors[1]["position"] = (selected_rotors[1]["position"] + 1) % 26
    if selected_rotors[1]["position"] == 0:
        selected_rotors[2]["position"] = (selected_rotors[2]["position"] + 1) % 26
        if selected_rotors[2]["position"] == 0:
            selected_rotors[3]["position"] = (selected_rotors[3]["position"] + 1) % 26

# The plugboard wiring
plugboard = {
    'A': 'Q',
    'B': 'D',
    'C': 'C',
    'D': 'B',
    'E': 'J',
    'F': 'X',
    'G': 'G',
    'H': 'H',
    'I': 'V',
    'J': 'E',
    'K': 'W',
    'L': 'U',
    'M': 'T',
    'N': 'N',
    'O': 'Y',
    'P': 'S',
    'Q': 'A',
    'R': 'R',
    'S': 'P',
    'T': 'M',
    'U': 'L',
    'V': 'I',
    'W': 'K',
    'X': 'F',
    'Y': 'O',
    'Z': 'Z'
}

# Forward pass through the rotors
def forward_rotors_encryption(char):
    for rotor in selected_rotors.values():
        char = rotor["wiring"][(ord(char) - ord('A') + rotor["position"]) % 26]
        char = chr((ord(char) - ord('A') - rotor["position"] + 26) % 26 + ord('A'))
    return char

# Reflector wiring
reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

# Reverse pass through the rotors
def reverse_rotors_encryption(char):
    for rotor in reversed(list(selected_rotors.values())):
        char = chr((rotor["wiring"].index(chr((ord(char) - ord('A') + rotor["position"]) % 26 + ord('A'))) + ord('A')))
        char = chr((ord(char) - ord('A') - rotor["position"]) % 26 + ord('A'))
    return char

# Encrypt and decrypt method
def encrypt_decrypt(char):
    rotor_step()
    new_char = plugboard[char]
    new_char = forward_rotors_encryption(new_char)
    new_char = reflector[(ord(new_char) - ord('A')) % 26]
    new_char = reverse_rotors_encryption(new_char)
    new_char = plugboard[new_char]
    return new_char

# The Text after encryption or decryption
result = ""

# Loop over the chars of the text to encrypt or decrypt them
for char in text:
    if char.isalpha():
        result += encrypt_decrypt(char)
    else:
        result += char

# Print the result
print("The encrypted/decrypted text is: ", result)