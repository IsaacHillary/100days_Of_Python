alphabet = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
'w', 'x', 'y', 'z'
]

import art
print(art.logo)


def cipher_caesar(direction, text, shift):
    if direction == "encode":
        encode = ""
        for i in text:
            if i not in alphabet:
                encode += i
            else:
                encode += alphabet[alphabet.index(i) + shift]
        print(f"The {direction}d text is: {encode}")

    elif direction == "decode":
        decode = ""
        for i in text:
            if i not in alphabet:
                decode += i
            else:
                decode += alphabet[alphabet.index(i) - shift]
        print(f"The {direction}d text is: {decode}")


restart = "yes"
while restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n")) % 26
        cipher_caesar(direction=direction, text=text, shift=shift)
        restart = input("Do yo want to restart?\nType 'yes' to restart\n").lower()
    else:
        print("Error, type either 'encode' or 'decode'")
