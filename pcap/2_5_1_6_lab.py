def ask_user_for_text_to_encrypt():
    return input('Text to encrypt: ')
    

def ask_user_for_code_point_offset():
    input_is_valid = False

    while not input_is_valid:
        try:
            user_input = int(input("Choose a shift value between 1 and 25 inclusive: "))
            if user_input not in range(1, 26):
                raise ValueError()
            input_is_valid = True
        except ValueError:
            print("Error: invalid shift value.")
    
    return user_input


def encrypt(text: str, code_point_offset: int):
    def encrypt_character(character: str):
        if not character.isalpha():
            return character
            
        base_code_point = ord('a') if character.islower() else ord('A')
        
        code_point = ord(character) - base_code_point
        code_point += code_point_offset
        code_point %= 26
        code_point += base_code_point
        
        character = chr(code_point)
        
        return character
        
    return "".join(map(encrypt_character, text))


if __name__ == "__main__":

    def main():
        text_to_encrypt = ask_user_for_text_to_encrypt()
        code_point_offset = ask_user_for_code_point_offset()
        encrypted_text = encrypt(text_to_encrypt, code_point_offset)
        print(encrypted_text)

    main()
