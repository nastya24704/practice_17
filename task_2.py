def translate_phrase() -> None:
    """
    Translates a phrase from Russian to English using a dictionary.

    The function reads:
    - N - number of word pairs
    - N lines with pairs (russian word, english word)
    - Phrase to translate

    Prints the translated phrase, words not in dictionary remain unchanged.
    """
    n = int(input("Enter the number of dictionary pairs: "))
    ru_en_dict = {}

    print("Enter word pairs (russian english):")
    for _ in range(n):
        ru, en = input().split()
        ru_en_dict[ru] = en

    phrase = input("Enter phrase to translate: ").split()
    translated = [ru_en_dict.get(word, word) for word in phrase]

    print("Translation:", ' '.join(translated))


if __name__ == "__main__":
    translate_phrase()
