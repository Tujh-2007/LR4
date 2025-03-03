for number in range(100, 1000):
    s = str(number)
    if len(s) == len(set(s)):
        print(number)