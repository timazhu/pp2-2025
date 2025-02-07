#Write a function that accepts string from user and print all permutations of that string

def permutations(s, start=0):
    if start == len(s) - 1:
        print(s)
        return

    for i in range(start, len(s)):
        s = list(s)
        s[start], s[i] = s[i], s[start]
        permutations(''.join(s), start + 1)
        s[start], s[i] = s[i], s[start]

permutations("abc")