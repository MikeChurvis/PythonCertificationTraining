def is_palindrome(text: str) -> bool:
    text = text.strip().replace(" ", "").lower()
    if not text:
        return False

    if text == text[::-1]:
        return True

    return False


if __name__ == "__main__":

    def main(override_user_input=None):
        user_input = override_user_input

        if user_input is None:
            user_input = input("Enter text to see if it's a palindrome: ")

        if is_palindrome(user_input):
            print("It's a palindrome")
        else:
            print("It's not a palindrome")

    main("Ten animals I slam in a net")
    main("Eleven animals I slam in a net")
