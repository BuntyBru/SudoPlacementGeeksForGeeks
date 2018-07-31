def perm(s):
    s = sorted(s)
    print(''.join(s), end=' ')
    while 1:
        first = -1  # First character from the right less then its next character
        second = -1  # Smallest character to the right of first and > than first
        for i in range(len(s) - 2, -1, -1):
            if s[i] < s[i + 1]:
                first = i
                print("inside the for loop of first = i ",first)
                break
        if first == -1:  # If the string is in non-increasing order, we have exhausted all the permutations
            break
        second = first + 1
        for i in range(second, len(s)):
            if s[first] < s[i] < s[second]:
                second = i
        s[first], s[second] = s[second], s[first]  # Swap first and second
        s = s[:first + 1] + s[:first:-1]  # Sort the substring after first
        print(''.join(s), end=' ')
    print()

    

s='AABC'
perm(s)