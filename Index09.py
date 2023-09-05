def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if int(s):
        return s
    if int(s)==0:
        return s
    if s==int(s):
        return -1
