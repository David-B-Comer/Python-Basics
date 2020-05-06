def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    """
    if first_string.lower() == second_string.lower():
        return False
    return sorted(first_string.lower()) == sorted(second_string.lower())

