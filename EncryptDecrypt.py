#EncryptDecrypt.py

#Author: Emil Bero

#Function that takes text and encrypts by adding 268 to a letters ascii number.
def encrypt(text):
    encrypted_text = ""
    for char in text:
        if char != ' ':
            encrypted_text += chr(ord(char) + 268)
        else:
            encrypted_text += char
    return encrypted_text

#Function that takes text and decrypts by adding 268 to a letters ascii number.
def decrypt(encrypted_text):
    decrypted_text = ""
    for char in encrypted_text:
        if char != ' ':
            decrypted_text += chr(ord(char) - 268)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    action = input("Enter 'encrypt' or 'decrypt': ").lower()
    #promt user to encrypt or decrypt text.
    if action == 'encrypt':
        file_name = input("Enter the name of the file to encrypt: ")
        with open(file_name, 'r') as file:
            plaintext = file.read()
        encrypted_text = encrypt(plaintext)
        with open('encryption.txt', 'w') as enc_file:
            enc_file.write(encrypted_text)
        print(f"Encryption complete. Check 'encryption.txt' for the result.")

    elif action == 'decrypt':
        file_name = input("Enter the name of the file to decrypt: ")
        with open(file_name, 'r') as file:
            encrypted_text = file.read()
        decrypted_text = decrypt(encrypted_text)
        with open('decryption.txt', 'w') as dec_file:
            dec_file.write(decrypted_text)
        print(f"Decryption complete. Check 'decryption.txt' for the result.")

    else:
        print("Invalid action. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()

