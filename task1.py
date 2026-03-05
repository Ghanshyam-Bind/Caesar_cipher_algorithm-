def caesar_cipher(text, shift, mode):
    result = ""
    
    if mode == "decrypt":
        shift = -shift
    
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        
        elif char.isdigit():
            new_digit = str((int(char) + shift) % 10)
            result += new_digit
        
        else:
            result += char
            
    return result

#input
message = input("Enter your message: ")
shift_value = int(input("Enter shift value: "))
choice = input("Type E 'encrypt' or D 'decrypt': ").lower()

output = caesar_cipher(message, shift_value, choice)

print("Result:", output)
