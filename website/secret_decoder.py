from getpass import getpass

text = str(input("Write encrypted_text here: "))
secret_key = str(getpass("Secret_key: "))

decrypted_text = ""
i = 0

if len(secret_key) == 4:
    for char in text:
        replaced_char_ascii = ord(char) - int(secret_key[i])
        replaced_char = chr(replaced_char_ascii)
        decrypted_text += replaced_char
        if i < 3:
            i += 1
            # print(f"added {i}")
        else:
            i = 0
            # print("returned to 0")

    print(decrypted_text)
else:
    print("Error: Secret_key Must be 4 digits long!")
