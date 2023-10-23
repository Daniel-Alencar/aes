from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def encrypt(plain_text, key):
    iv = get_random_bytes(16)
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv)
    plain_text = plain_text + " " * (16 - len(plain_text) % 16)
    cipher_text = cipher.encrypt(plain_text.encode())
    return base64.b64encode(iv + cipher_text).decode()

def decrypt(cipher_text, key):
    cipher_text = base64.b64decode(cipher_text.encode())
    iv = cipher_text[:16]
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv)
    plain_text = cipher.decrypt(cipher_text[16:]).decode('utf-8')
    return plain_text.rstrip(" ")

def main():
    choice = input("Escolha uma opção\n1- Encriptação\n2- Decriptação\nEscolha: ")

    if choice == '1':
        key = input("Chave (32 caracteres): ")
        with open('message.txt', 'r') as file:
            message = file.read()

        if len(key) != 32:
            print("A chave deve ter 32 caracteres!")
            return

        encrypted = encrypt(message, key)
        with open('encrypted.txt', 'w') as file:
            file.write(encrypted)
    
    elif choice == '2':
        key = input("Chave (32 caracteres): ")
        with open('message.txt', 'r') as file:
            ciphertext = file.read()

        if len(key) != 32:
            print("A chave deve ter 32 caracteres!")
            return

        decrypted = decrypt(ciphertext, key)
        with open('decrypted.txt', 'w') as file:
            file.write(decrypted)
    
    else:
        print("Escolha inválida!")

if __name__ == '__main__':
    main()
