"""
credits for original algorithm: antonioam82
"""
import random
import os

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

cifrad = ""

def encode(text, key):
    cifrad = ""
    random.seed(key)
    for c in text:
        if c in abc:
            r = random.randint(1,100)
            cifrad += abc[(abc.index(c) + r) % len(abc)]
        else:
            cifrad += c
    return cifrad


def decoded(text, key):
    cifrad = ""
    random.seed(key)
    for c in text:
        if c in abc:
            r = random.randint(1,100)
            cifrad += abc[(abc.index(c) - r) % len(abc)]
        else:
            cifrad += c
    return cifrad


def clear():
    os.system("clear")


while True:
    clear()
    print("Algorithm of Caesar Cipher\n")
    print("1. Encrypt message.")
    print("2. Decrypt message.")
    print("3. Exit.\n")
    opc = int(input("Enter option: "))
    if opc == 1:
        text = input("Enter your message: ")
        key = int(input("Enter the key: "))
        ctext = encode(text, key)
        print("Ciphertext: ", ctext)
        input("Press Enter to continue...")
    elif opc == 2:

        text = input("Enter your message: ")
        key = int(input("Enter the key: "))
        ctext = decoded(text, key)
        print("Decrypt text: ", ctext)
        input("Press Enter to continue...")
    elif opc == 3:
        break
    else:
        input("Invalid option, press Enter to continue...")
