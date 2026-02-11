def stringAddition(num1: str, num2: str) -> str:
    res1 = 0
    res2 = 0
    i = 0

    for char in num1[i:]:
        int_val = ord(char) - ord('0')
        res1 = res1 * 10 + int_val

    for char in num2[i:]:
        int_val = ord(char) - ord('0')
        res2 = res2 * 10 + int_val
    
    return str(res1 + res2)