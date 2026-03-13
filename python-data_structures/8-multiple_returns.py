#!/usr/bin/python3
def multiple_returns(sentence):
    """Sətrin uzunluğunu və ilk hərfini kortej olaraq qaytarır."""
    length = len(sentence)
    if length == 0:
        first_char = None
    else:
        first_char = sentence[0]
    return (length, first_char)
