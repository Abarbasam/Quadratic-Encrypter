#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
import string

a = randint(2, 3)
b = randint(1, 2)
c = randint(0, 10)


message = str(raw_input("Enter your message\n> "))
encrypted_Message = []

for i in a, b, c:
    encrypted_Message.append(str(len(str(i))))
    encrypted_Message.append(str(i))


for i in message:
    x = ord(i)
    new_ASCII_Value = ((a * (x**2)) + (b * x) + c)
    encrypted_Message.append(str(len(str(new_ASCII_Value))))
    encrypted_Message.append(str(new_ASCII_Value))

encrypted_Message = "".join(encrypted_Message)
print encrypted_Message
