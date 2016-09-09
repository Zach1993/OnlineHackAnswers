def longestPalindrome(s):
    length = len(s)
    space = length  # or a-b
    a = 0
    b = a + space
    inc = 1
    # base case, if true stop while loop return str
    str = s
    str_r = s[::-1]

    while str != str_r:
        a = 0
        space = space - 1
        b = a + space
        str = s[a:b]
        str_r = str[::-1]

        while b <= length and str != str_r:
            b = b + 1
            a = a + 1
            str = s[a:b]
            str_r = str[::-1]

    return str
