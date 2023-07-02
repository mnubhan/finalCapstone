import string
""" This program will take a message and cypher it """
input_msg = input("Please enter a message to cypher: ")
""" Handle ASCII values that exceed 90 or 122 """
def exceed_ascii(x):
    return x - 26
""" Handle characters that are letters """
def handle_char(x):
    if x.isupper():
        upperASCII = ord(x)+15
        if upperASCII > 90:
            return chr(exceed_ascii(upperASCII)).upper()
        else:
            return chr(upperASCII).upper()
    else:
        lowerASCII = ord(x)+15
        if lowerASCII > 122:
            return chr(exceed_ascii(lowerASCII))
        else:
            return chr(lowerASCII)
""" The main function for cypher the message """
def cypher(msg):
    cypher_msg = ""
    for char in msg:
        if char in string.punctuation:
            cypher_msg += char
        elif char == " ":
            cypher_msg += char
        elif isinstance(char, str):
            cypher_msg += handle_char(char)
        elif isinstance(float(char), int):
            cypher_msg += char
        elif isinstance(float(char), float):
            cypher_msg += char
    return f"Your cyphered message is: {cypher_msg}"
print(cypher(input_msg))

