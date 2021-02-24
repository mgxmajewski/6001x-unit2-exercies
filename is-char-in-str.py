def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    """
    if aStr == "":
        return False
    test_char = aStr[len(aStr)//2]
    if char == test_char:
        return True
    elif len(aStr) == 1:
        return False
    else:
        if test_char > char:
            return isIn(char, aStr[:len(aStr)//2])
        elif test_char < char:
            return isIn(char, aStr[len(aStr)//2:])
    return isIn(char, aStr)



print(isIn('a', 'abcdefghijklmnop'))
