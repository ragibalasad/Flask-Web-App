from getpass import getpass

text = str(input("Type your message: "))
secret_key = str(getpass("Set a 4 digit Secret_key: "))

encrypted_text = ""
i = 0

if len(secret_key) == 4:
    for char in text:
        replaced_char_ascii = ord(char) + int(secret_key[i])
        replaced_char = chr(replaced_char_ascii)
        encrypted_text += replaced_char
        if i < 3:
            i += 1
            # print(f"added {i}")
        else:
            i = 0
            # print("returned to 0")

    print(encrypted_text)
else:
    print("Error: Secret_key Must be 4 digits long!")
