CHARACTER_DISPLAY_ENCODINGS = (
    "###,# #,# #,# #,###".split(","),  # 0
    "  #,  #,  #,  #,  #".split(","),  # 1
    "###,  #,###,#  ,###".split(","),  # 2
    "###,  #,###,  #,###".split(","),  # 3
    "# #,# #,###,  #,  #".split(","),  # 4
    "###,#  ,###,  #,###".split(","),  # 5
    "###,#  ,###,# #,###".split(","),  # 6
    "###,  #,  #,  #,  #".split(","),  # 7
    "###,# #,###,# #,###".split(","),  # 8
    "###,# #,###,  #,###".split(","),  # 9
)


def get_user_input():
    user_input = input("Enter a non-negative integer number: ").strip()
    if not user_input.isdigit():
        raise ValueError()
    return user_input


def main():
    try:
        user_input = get_user_input()
    except ValueError:
        print("Your input is not a non-negative integer number.")
        return

    encoded_digits = [CHARACTER_DISPLAY_ENCODINGS[int(digit)] for digit in user_input]

    display_rows = [
        " ".join(digit_display_data[row] for digit_display_data in encoded_digits)
        for row in range(5)
    ]

    display = "\n".join(display_rows)

    print(display)


if __name__ == "__main__":
    main()
