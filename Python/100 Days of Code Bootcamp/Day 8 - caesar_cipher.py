#Ioannis Apomachos

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    encrypted_text=""
    for letter in text:
        if letter in alphabet:
            encrypted_text += alphabet[alphabet.index(letter)+shift-26]
        else:
            encrypted_text += letter
    print(f"The encoded text is {encrypted_text}")

def decrypt(text, shift):
    decrypted_text=""
    for letter in text:
        if letter in alphabet:
            decrypted_text += alphabet[alphabet.index(letter)-shift]
        else:
            encrypted_text += letter  
    print(f"The encoded text is {decrypted_text}")


keep_running=True

while keep_running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26


    if direction=="encode":
        encrypt(text,shift)
    elif direction=="decode":
        decrypt(text,shift)
    else:
        print("Wrong direction input. Please Type 'encode' or 'decode' ")
    
    result=input("Type yes if you want to go again. Otherwise type no ")
    if result=="no":
        keep_running=False

print("Goodbye")
