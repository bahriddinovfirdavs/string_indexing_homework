def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if s[0] in 'qwertyuiopasdfghjkzxcvbnm':
        return -1
    return int(s)
print(main(str(input())))

