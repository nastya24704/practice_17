from typing import Dict, List


def count_descendants(tree: Dict[str, List[str]], person: str) -> int:
    """
    Recursively counts the number of descendants for a given person.

    Args:
        tree (Dict[str, List[str]]): Dictionary where key is parent, value is list of children
        person (str): Name of the person to count descendants for

    Returns:
        int: Total number of descendants (children, grandchildren, great-grandchildren, etc.)
    """
    if person not in tree:
        return 0

    total = len(tree[person])
    for child in tree[person]:
        total += count_descendants(tree, child)

    return total


def count() -> None:
    """
    Determines the number of descendants for a given person in a family tree.

    The function reads:
    - N - number of parent-child relationships
    - N lines with pairs (parent child)
    - Person name to count descendants for

    Prints the total number of descendants.
    """
    n = int(input("Enter the number of parent-child relationships: "))
    tree: Dict[str, List[str]] = {}

    print("Enter pairs (parent child):")
    for _ in range(n):
        parent, child = input().split()
        if parent not in tree:
            tree[parent] = []
        tree[parent].append(child)

    target = input("Enter name to count descendants for: ").strip()
    result = count_descendants(tree, target)

    print(f"Number of descendants for {target}: {result}")


if __name__ == "__main__":
    count()
