import readline
from math import sqrt

#encrypted_Message = ""
encrypted_Message = str(raw_input("Enter your encrypted message\n> "))
encrypted_Message = list(encrypted_Message)

cursor = 0
variables = []


for i in range(3):
    temp = []
    read_Digits = int(encrypted_Message[cursor])
    cursor += 1

    for j in range(read_Digits):
        temp.append(encrypted_Message[cursor])
        cursor += 1
    temp = int("".join(temp))
    variables.append(temp)

a = variables[0]
b = variables[1]
c = variables[2]

encrypted_Words = []
while cursor < len(encrypted_Message):
    temp = []
    read_Digits = int(encrypted_Message[cursor])
    cursor += 1

    for j in range(read_Digits):
        temp.append(encrypted_Message[cursor])
        cursor += 1
    temp = "".join(temp)
    encrypted_Words.append(int(temp))

decrypted_Words = []

for i in encrypted_Words:
    c_Val = c - i
    word = int(((-1 * b) + sqrt((b**2) - (4 * a * c_Val))) / (2 * a))
    word = chr(int(word))
    decrypted_Words.append(word)
    
print "".join(decrypted_Words)
