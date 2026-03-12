def antonym() -> None:
    """
    Finds the antonym for a given word.

    The function reads:
    - N - number of antonym pairs
    - N lines with antonym pairs
    - Word to find antonym for

    Prints the antonym or the original word if antonym is not found.
    """
    n = int(input("Enter the number of antonym pairs: "))
    antonyms = {}

    print("Enter antonym pairs:")
    for _ in range(n):
        word1, word2 = input().split()
        antonyms[word1] = word2
        antonyms[word2] = word1

    target = input("Enter word to find antonym for: ").strip()
    result = antonyms.get(target, target)

    print(f"Antonym: {result}")


if __name__ == "__main__":
    antonym()
