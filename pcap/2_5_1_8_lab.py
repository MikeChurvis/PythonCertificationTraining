def are_anagrams(first_word: str, second_word: str) -> bool:
    first_word, second_word = tuple(
        map(
            lambda word: "".join(sorted(word.strip().replace(" ", "").lower())),
            (first_word, second_word),
        )
    )

    if first_word == second_word:
        return True

    return False


if __name__ == "__main__":

    def main():
        first_word = input("Pick a word: ")
        second_word = input("Pick a second word: ")
        words_are_anagrams = are_anagrams(first_word, second_word)

        if words_are_anagrams:
            print("Anagrams")
        else:
            print("Not anagrams")

    main()
